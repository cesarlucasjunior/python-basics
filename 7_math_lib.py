# we have some particularities in Python regarding math operations:

# like, divisions in python are decimal by default
n = 5/2
print(n) # 2.5

# if we want an int result we have to use (//)
n = 5//2
print(n) # 2 (slash down)  

# when dividing by negative numbers, most other languages round close to zero, while 
# python slash down
n = -5/2
print(n) # -3
n = -5//2
print(n) # -3

# to adjust this behavior:
print(int(-5/2)) #-2

# module
print(10%3) #1

# if negativa, python slash
print(-10%3) #2

import math
#adjusting this behavior
print(math.fmod(-10,3))

# Some Math helpers:
print("-----------------------")

# Round down:
print(math.floor(3/2)) #1
# Round up:
print(math.ceil(3/2)) #2
# square root:
print(math.sqrt(2)) #1.41
# potentiation:
print(math.pow(2,3)) #8.0
# max / min
print(float("inf") > 8980980)
print(float("-inf"))