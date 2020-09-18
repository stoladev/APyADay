import torch

x = torch.arange(6).reshape(3, 2)
print(x)

print(type(x[1, 1]))

x = torch.arange(10)

# View and reshape are very similar.
print(x.view(2, 5))
print(x)
print(x.reshape(2, 5))
print(x)

# This finally changes it.
x = x.reshape(2, 5)
print(x)

# This view example can infer what the 2nd dimension will be.
x = torch.arange(10)
print(x.shape)
print(x.view(2, -1))

a = torch.tensor([1., 2., 3.])
b = torch.tensor([4., 5., 6.])

# Arithmetic functions with an underscore operator reassign the variable after the calculation.
print(a + b)
print(a.mul(b))
print(a.mul_(b))
# a = a + b
