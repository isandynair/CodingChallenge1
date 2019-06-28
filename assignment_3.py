import numpy as np

# Problem 1
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(np.where(arr%2==1, -1, arr))

# Problem 2
arr = np.arange(10).reshape(2,5)
print(arr)

# Problem 3
arr = np.array([1,2,3])
result = np.concatenate((np.repeat(arr,3),np.tile(arr,3)))
print(result)

# Problem 4
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
res = np.intersect1d(a,b)
print(res)

# Problem 5
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
r = np.array(np.where(a==b))
print(r)

# Problem 6
r = 5 * np.random.random_sample((5, 3)) + 5
print(r)

# Problem 7
np.set_printoptions(threshold=3)
arr = np.arange(15)
print(arr)

# Problem 8
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)
print(rand_arr)

# Problem 9
arr = np.arange(9).reshape(3,3)
arr[:,[0, 1]] = arr[:,[1, 0]]
print(arr)

# Problem 10
arr = np.arange(9).reshape(3,3)
arr[[0, 1],:] = arr[[1, 0],:]
print(arr)

