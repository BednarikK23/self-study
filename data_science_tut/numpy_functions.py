import numpy as np

a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 7]
])

print(np.sin(a))
# cos(a)
# tan(a)
# sqrt(a)
# arctan(a)
# arccos(a)
# arcsin(a)

# key statistics of matrix:
print(a.sum())
# a.max(), a.min()
print(a.mean())  # sum of numbers divided by count of numbers
print(np.median(a))
print(np.std(a))  # how much on average are numbers diviating from median

a = np.array([
        [1, 2, 3, 0],
        [4, 5, 6, 0],
        [9, 8, 7, 0]
])

a = a.reshape((2, 6))  # have to be possible
print(a)
a = a.reshape((2, 3, 2))
print(a)
print(a.transpose())  # turns around the order - change dimensions
print(a.flatten())  # 1D

for x in a.flat:  # just attribute that returns flatten version of array
    print(x)


b = np.array([
        [10, 200, 30, 10],
        [40, 50, 60, 110],
        [90, 80, 70, 220]
])

a = a.reshape(b.shape)
c = np.concatenate((a, b))
print(c)
c2 = np.stack((a, b))  # creates another dimension for the second array
print(c2)
print(c.shape, c2.shape)

a = np.array([
        [1, 2, 3, 0],
        [4, 5, 6, 0],
        [9, 8, 7, 0],
        [8, 5, 3, 1]
])

print(np.split(a, 4))  # split the array into equal parts...
# .asplit(())
b = np.array([100, 200, 300, 400])

a = np.append(a, [b], axis=0)
print(a)
a = np.insert(a, 1, b, axis=0)
print(a)

