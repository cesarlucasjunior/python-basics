# Some function to use with lists:
arr = [1,2,3,4,5,6]

#reversing elements
arr.reverse()
print(arr)

#sorting elements
messy_list = [4,6,1,3,2,9,7,5,8]
messy_list.sort()
print(messy_list)
messy_list.sort(reverse=True)
print(messy_list)

messy_list = ['joao', 'batista', 'ana', 'luiz', 'Edu']
messy_list.sort()
print(messy_list)

#custom sort
messy_list.sort(key=lambda x: len(x))
print(messy_list)

#list comprehension: another way to initializa a list
arr = [i for i in range(5)]
print(arr)
arr = [i*i for i in range(5)]
print(arr)

#2-d list
arr2d = [[0]*4 for i in range(4)]
print(arr2d)