# lists are the arrays in python.

#declarion and assignment
arr = [1, 2, 3, 4, 5]
arrText = ["ana", "maria", "josé", "carlos", "andresa"]

print(arr)
print(arrText)

#adding values at the end of the list
arr.append(6)
arr.append(7) 
print(arr)
#removing the last item
arr.pop()
print(arr) #Big O (1)

#lists can be used as a stack
arr.insert(2, 7)
print(arr) #Big O (n)

#reassinging
arr[2] = 3
print(arr)