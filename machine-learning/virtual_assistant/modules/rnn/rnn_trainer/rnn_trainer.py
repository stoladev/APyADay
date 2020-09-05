import random
import os
import torch
import torch.nn as nn

from modules.rnn.rnn_tools.rnn_mask_checker import check_mask_loss

from modules.handlers.data_handler.data_cleaner import (
    convert_batch_to_training_data,
)

from modules.handlers.learning_handler import (
    device,
    teacher_forcing_ratio,
    SOS_token,
    hidden_size,
    loadFilename,
)


def train(
    input_variable,
    lengths,
    target_variable,
    mask,
    max_target_len,
    encoder,
    decoder,
    encoder_optimizer,
    decoder_optimizer,
    batch_size,
    clip,
):

    # Zero gradients
    encoder_optimizer.zero_grad()
    decoder_optimizer.zero_grad()

    # Set device options
    input_variable = input_variable.to(device)
    lengths = lengths.to(device)
    target_variable = target_variable.to(device)
    mask = mask.to(device)

    # Initialize variables
    loss = 0
    print_losses = []
    n_totals = 0

    # Forward pass through encoder
    encoder_outputs, encoder_hidden = encoder(input_variable, lengths)

    # Create initial decoder input (start with SOS tokens for each sentence)
    decoder_input = torch.LongTensor([[SOS_token for _ in range(batch_size)]])
    decoder_input = decoder_input.to(device)

    # Set initial decoder hidden state to the encoder's final hidden state
    decoder_hidden = encoder_hidden[: decoder.n_layers]

    # Determine if we are using teacher forcing this iteration
    use_teacher_forcing = True if random.random() < teacher_forcing_ratio else False

    # Forward batch of sequences through decoder one time step at a time
    if use_teacher_forcing:
        for t in range(max_target_len):
            decoder_output, decoder_hidden = decoder(
                decoder_input, decoder_hidden, encoder_outputs
            )
            # Teacher forcing: next input is current target
            decoder_input = target_variable[t].view(1, -1)
            # Calculate and accumulate loss
            mask_loss, n_total = check_mask_loss(
                decoder_output, target_variable[t], mask[t]
            )
            loss += mask_loss
            print_losses.append(mask_loss.item() * n_total)
            n_totals += n_total
    else:
        for t in range(max_target_len):
            decoder_output, decoder_hidden = decoder(
                decoder_input, decoder_hidden, encoder_outputs
            )

            # No teacher forcing: next input is decoder's own current output
            _, topi = decoder_output.topk(1)
            decoder_input = torch.LongTensor([[topi[i][0] for i in range(batch_size)]])
            decoder_input = decoder_input.to(device)
            # Calculate and accumulate loss
            mask_loss, n_total = check_mask_loss(
                decoder_output, target_variable[t], mask[t]
            )
            loss += mask_loss
            print_losses.append(mask_loss.item() * n_total)
            n_totals += n_total

    loss.backward()

    # Clip gradients: gradients are modified in place
    _ = nn.utils.clip_grad_norm_(encoder.parameters(), clip)
    _ = nn.utils.clip_grad_norm_(decoder.parameters(), clip)

    # Adjust model weights
    encoder_optimizer.step()
    decoder_optimizer.step()

    return sum(print_losses) / n_totals


def train_iterations(
    model_name,
    voc,
    pairs,
    encoder,
    decoder,
    encoder_optimizer,
    decoder_optimizer,
    embedding,
    encoder_n_layers,
    decoder_n_layers,
    save_dir,
    n_iteration,
    batch_size,
    print_every,
    save_every,
    clip,
    corpus_name,
    load_filename,
):

    # Load batches for each iteration
    training_batches = [
        convert_batch_to_training_data(
            voc, [random.choice(pairs) for _ in range(batch_size)]
        )
        for _ in range(n_iteration)
    ]

    # Initializations
    print("Initializing ...")
    start_iteration = 1
    print_loss = 0
    if load_filename:
        checkpoint = torch.load(loadFilename)
        start_iteration = checkpoint["iteration"] + 1

    # Training loop
    print("Training...")
    for iteration in range(start_iteration, n_iteration + 1):
        training_batch = training_batches[iteration - 1]
        # Extract fields from batch
        input_variable, lengths, target_variable, mask, max_target_len = training_batch

        # Run a training iteration with batch
        loss = train(
            input_variable,
            lengths,
            target_variable,
            mask,
            max_target_len,
            encoder,
            decoder,
            encoder_optimizer,
            decoder_optimizer,
            batch_size,
            clip,
        )
        print_loss += loss

        # Print progress
        if iteration % print_every == 0:
            print_loss_avg = print_loss / print_every
            print(
                "Iteration: {}; Percent complete: {:.1f}%; Average loss: {:.4f}".format(
                    iteration, iteration / n_iteration * 100, print_loss_avg
                )
            )
            print_loss = 0

        # Save checkpoint
        if iteration % save_every == 0:
            directory = os.path.join(
                save_dir,
                model_name,
                corpus_name,
                "{}-{}_{}".format(encoder_n_layers, decoder_n_layers, hidden_size),
            )
            if not os.path.exists(directory):
                os.makedirs(directory)
            torch.save(
                {
                    "iteration": iteration,
                    "en": encoder.state_dict(),
                    "de": decoder.state_dict(),
                    "en_opt": encoder_optimizer.state_dict(),
                    "de_opt": decoder_optimizer.state_dict(),
                    "loss": loss,
                    "voc_dict": voc.__dict__,
                    "embedding": embedding.state_dict(),
                },
                os.path.join(directory, "{}_{}.tar".format(iteration, "checkpoint")),
            )
