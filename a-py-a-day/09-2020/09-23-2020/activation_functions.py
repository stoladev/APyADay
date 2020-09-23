"""
x * w + b

W implies how much weight or strength to give the incoming input
B is an offset value, making x*w have to reach a certain threshold before having an effect

Example: b = -10

The effects of x*w won't start to overcome the bias until their product surpasses 10
Then, the effect is solely based on the value of w

Sigmoid function:
    - f(z) = 1/1+e^(-z)

Hyperbolic tangent:
    - tanh(z)
    - Outputs between -1 and 1 instead of 0 and 1
    - cosh x = (e^x + e^-x) / 2
    - sinh x = (e^x + e^-x) / 2
    - tanh x = sinh x / cosh x

Rectified linear unit (ReLU):
    - max(O, z)
    - ReLU has great performance, especially when dealing with vanishing gradient




"""
