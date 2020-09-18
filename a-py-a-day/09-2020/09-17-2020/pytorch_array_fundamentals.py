"""

Single number - Scalar.
1D - Vector.
2D - Matrix.
3D+ - Tensor.

"""

import numpy as np
import torch

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

x = torch.from_numpy(arr)
print(type(x))

arr2d = np.arange(0.0, 12.0)
print(arr2d)

x2 = torch.from_numpy(arr2d)
print(x2)

# Direct link is made with array. Most of the time you want to avoid this.
# Simplify to torch.tensor.
my_arr = np.arange(0, 10)
safe_tensor = torch.tensor(my_arr)
directly_linked_tensor = torch.from_numpy(my_arr)

print(my_arr)
my_arr[0] = 100
print(safe_tensor)
print(directly_linked_tensor)

# torch.tensor creates a copy in the memory instead of calling.

# Difference between torch.Tensor vs torch.tensor
# Tensor converts to floating point. Interchangeable with torch.FloatTensor(new_arr)

new_arr = np.array([1, 2, 3])
torch.tensor(new_arr)
# torch.Tensor(new_arr) - returns float

# Want 0s? torch.zeros(4, 3)
torch.empty(4, 2)

# You can easily reassign data types
my_tensor = torch.tensor([1, 2, 3])
print(my_tensor.type(torch.int32))

# All between 0-1 are likely to be picked.
print(torch.rand(4, 3))

# Mean is 0, standard deviation of 1.
print(torch.randn(4, 3))

# Returns from low (inclusive) to high (exclusive)
print(torch.randint(low=0, high=10, size=(5, 5)))

# Examples:
x = torch.zeros(2, 5)
print(torch.rand_like(x))
print(torch.randn_like(x))
print(torch.randint_like(x, low=0, high=10))

# Set a seed to use same random values
# Seed is arbitrary number to use for consistency
torch.manual_seed(42)
print(torch.rand(2, 3))
