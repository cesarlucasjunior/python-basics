#initializing array on 'n' size with default value of 1
n = 5
arr = [1] * n 
print(arr)

#size of an list/array:
print(len(arr))

#acessing array by last indexes:
arr = [1, 2, 3, 4, 5]
print(arr[-1])
print(arr[-2])

#creating a sublist - slicing
subArray = arr[0:3]
print(subArray)

#unpacking - is a way to assign a array value to a variable
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

#looping through array
print("---------PRINTING---------")
nums = [1, 2, 3, 4, 5, 6]

# looping using index
for i in range(len(nums)):
    print(nums[i])

# looping using elements
for num in nums:
    print(num)

# looping using indexes and elements with unpacking
for i, num in enumerate(nums):
    print(i, '-', num)

#unpacking multiples arrays in the same time:
arr1 = [1,2,3]
arr2 = [4,5,6]

for a1, a2 in zip(arr1, arr2):
    print(a1, a2)