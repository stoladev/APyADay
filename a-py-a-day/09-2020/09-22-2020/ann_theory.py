"""
Theory topics:
    - Perceptron model to neural networks
    - Activation functions
    - Cost functions
    - Feed forward networks
    - Back propagation

Programming topics:
    - Gradients
    - Linear regression
    - Datasets
    - Full artificial neural networks
        - Regression
        - Classification

Perceptron model:
    - Example: 2 data points go into an equation, outputs some y
    - Each input has its own weights (a + b = y turns into ax + bx = y)
    - A bias term is added so that the inputs can have more options ((ax + z) + (bx + z) = y)
    - To build a network of perceptrons:
        - Connect layers of perceptrons using a multi-layer perceptron model
    - The outputs of one perceptron are directly fed into as inputs to another perceptron
    - This allows the network as a whole to learn about interactions and relationships between features

Layers:
    - The first layer is the input layer
    - The last layer is the output layer (this layer can be more than one neuron)
    - Any layers in between are called hidden layers
    - Hidden layers are difficult to interpret, due to their high interconnectivity
    - Hidden layers are separate from any known input or output values

When does a neural network become a "deep" neural network?
When it contains 2 or more hidden layers.




"""
