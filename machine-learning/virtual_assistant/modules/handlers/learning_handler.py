import os
import torch

# Directories
data_directory = "training_data"
voc_directory = os.path.join("data", "save")
data = os.path.join(data_directory)
datafile = os.path.join(data, "conversation_data.txt")

# Cuda and device setup
USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

# General model configuration
use_existing_model = True
model_name = "cb_model"
attn_model = "dot"
# attn_model = "general"
# attn_model = "concat"
hidden_size = 500
encoder_n_layers = 2
decoder_n_layers = 2
dropout = 0.1
batch_size = 64
PAD_token = 0  # Used for padding short sentences
SOS_token = 1  # Start-of-sentence token
EOS_token = 2  # End-of-sentence token
MIN_COUNT_FOR_TRIM = 1  # Minimum word count threshold for trimming
MAX_LENGTH = 10  # Maximum sentence length to consider

# Training/optimization
clip = 50.0
teacher_forcing_ratio = 1.0
learning_rate = 0.0001
decoder_learning_ratio = 5.0
n_iteration = 100
checkpoint_iter = 100
save_every = 50
print_every = 5


# Loading/creating  the model
if use_existing_model:
    loadFilename = os.path.join(
        voc_directory,
        model_name,
        data_directory,
        "{}-{}_{}".format(encoder_n_layers, decoder_n_layers, hidden_size),
        "{}_checkpoint.tar".format(checkpoint_iter),
    )
else:
    loadFilename = None
