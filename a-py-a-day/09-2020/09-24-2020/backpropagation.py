"""
How do the cost function results change with respect to the weights in the network?

Simple network:
o-o-o-o

Each input receives a weight an a bias:
o-w1+b1-o-w2+b2-o-w3+b3-o

This means we have:
C(w1, b1, w2, b2, w3, b3)

Let's say we have L layers, then our notation becomes:
o    o      o     o
L-n | L-2 | L-1 | L

Focusing on the last two layers:
z=wx+b
Then we apply an activation function we'll state:
a = o(z)

This means we have:
z^L = w^La^(L-1)+b^L
a^L = o(z^L)

Using some calculus notation, we can expand this idea to networks with multiple neurons per layer
An example would be the 'Hadamard Product', which is elements by elements calculation

Learning process summed up:
    - Use input x to set the activation function a for the input layer
    - z = wx+b
    - a = o(z)
    - This resulting a then feeds into the next layer, and so on
    - For each layer, compute:
    - z^L = w^La^(L-1)+b^L
    - a^L = o(z^L)
    - Compute the error vector
    - Back-propagate the error
    - Take the Hadamard product. This moves the error backward through the activation function in layer l, giving us
    the error in weighted input to layer l.
    - This allows us to adjust the weights and biases to help minimize that cost function

"""
