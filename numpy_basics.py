import numpy as np
from random import random

arr = np.array([1, 2, 3, 4, 5], dtype='int32')
print(arr[2])

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[1, 2])
# Finding dimensions of an array
print(arr2d.ndim)
print(arr2d.shape)
print(arr.shape)
print(arr2d.size)
print(arr2d.dtype)
arr[2] = 10
print(arr)
arr = np.append(arr, 15)
print(arr)

# Initializing arrays

array = np.zeros(5)
zeros2d = np.zeros((5, 5))
print(array)
print(zeros2d)
ones3d = np.ones((5, 5, 5))
print(ones3d)

fullArr = np.full((3, 3), 7)
print(fullArr)
fullArr[1, 1] = 2
print(fullArr)

rand = np.random.rand(3, 3)
print(rand)
randInt = np.random.randint(1, 100, (3, 3))
print(randInt)

repeatedArr = np.repeat(randInt, 3, axis=0)
print(repeatedArr)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
print(arr1 + arr2)
print(arr1 ** 2)

print("------ HOMEWORK ------")



# Construct an array: 
# 00000
# 11111
# 00000
# 11111
# 00700
# 11111
# Make it with as little code as possible.

theArr = np.zeros((6, 5))
j = 1
for i in range(3):
    theArr[j] = [1, 1, 1, 1, 1]
    j += 2
theArr[4, 2] = 7
print(theArr)

# Accept 5 numbers from user, then accept a number with which all values will be multiplied.

numArr = np.array([])
for i in range(5):
    inp = int(input("Enter a number: "))
    numArr = np.append(numArr, inp)
factor = int(input("What do you want to multiply the numbers with? Enter number: "))
result = numArr * factor
print(result)
