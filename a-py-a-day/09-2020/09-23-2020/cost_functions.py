"""
Take the estimated outputs of the network and then compare them to the real values of the label

Cost function (loss function/error function): must be an average so it can output a single value

We can keep track of this during training.

y to represent the true value
a to represent neuron's prediction
w * x + b = z

Pass z into activation function o(z) = a

Very common cost function (quadratic cost function):
    - We calculate the difference between the real values y(x) against our predicted values a(x)

Think of the cost function as:
    - C(W, B, S^r, E^r)
    - W is our neural network's weights
    - B is the neural network's biases
    - S^r is the input of a single training sample
    - E^r is the desired output of that training sample

a(x) holds information about weights and biases.
This means that we can expect C to be quite complex, with huge vectors of weights and biases, in a large network

This means we have some cost function C dependent lots of weights
    - C(w1, w2, w3, ... wn)

Aim to minimize our loss/cost (overall error)
Figure out what value of w results in the minimum of C(w)

Larger steps are faster in the learning process, but we risk overshooting the minimum
That is called the 'learning rate'

We could start with larger steps and then go smaller as we realize the slope gets closer to zero
This is known as 'adaptive gradient descent'

'Adam' is an efficient way of searching for these minimums. It is 'A Method for Stochastic Optimization'.

When dealing with N-dimensional vectors (tensors), the notation changes from derivative to gradient
This means we calculate (gradient)C(w1, w2, ... wn)

For classification problems, we use the 'cross entropy' loss function
The assumption is that your model predicts a probability distribution p(y=i) for each class i=1, 2, ..., C

For a binary classification, this results in:
-(ylog(p) + (1 - y)log(1 - p))
For M number of classes > 2, use cross entropy

"""
