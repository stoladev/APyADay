"""
Non-exclusive classes:
    - A single data point can have multiple classes/categories assigned to it
    - (ex) Photos can have multiple tags

Mutually exclusive classes:
    - Only one class per data point
    - (ex) Photos can either be grayscale or not

Organizing multiple classes:
    - One-hot encoding
    - Uses binary classification for data point sets (or dummy variables)

When dealing with non-exclusive, default to using the Sigmoid function
Each neuron will output 0 or 1, indicating the probability of having that class assigned to it

For mutually exclusive classes, we can use the softmax function
    - Softmax function calculates the probabilities distribution of the event over K different events
    - This function will calculate the probabilities of each target class over all possible target classes
    - Range will be 0 to 1, and the sum of all the probabilities will be equal to one
    - The model returns the probabilities of each class and the target class chosen will have highest probability
    - The output should look similar to this example:
        - [Red, Green, Blue]
        - [0.1, 0.6, 0.3]

"""
