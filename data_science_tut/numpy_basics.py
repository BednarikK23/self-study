import numpy as np

# simillar to list but acts diferently cause numpy is for science, linear algebra and so oon..
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a[0])
print(b[1])
print(a.shape)

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

# doesnt concate these arrays but does coomputations and return 4 dimensional vector again...
print(x + y)

# fills
arr = np.zeros((5, 7, 3))
arr1 = np.ones((5, 7, 3))
arr2 = np.full((5, 7, 3), 9)
print(arr, "\n", arr1, "\n", arr2)
# also np.empty() - with not initialized values but not really what we usually want

# completly random nubers between 0-1, usefull in training
r = np.random.random((5, 5))
print(r)

x = np.arange(0, 1000, 5)  # other way to do array
xx = np.linspace(0, 1000, 100)  # minimum, maximum, hom many values ve wanna create evenly distributed in this range
y = x * 2 - x ** 2
print(y)
print(xx)

ll = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
], dtype=float)  # can specify type of elems
print("Dimension of ll: ", ll.ndim, " ; count of elements: ", ll.size, \
      " elems are type: ", ll.dtype)
