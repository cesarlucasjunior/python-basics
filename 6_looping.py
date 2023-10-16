# In python, we have two types of repetition structure:

# while:
n = 0
while n < 5:
    print(n)
    n+=1

print('----------------------')
# for:
for i in range(5):
    print(i)
    # 0, 1, 2, 3, 4
    # in this case we have: starting with 0, 5 not included, auto incremented.

print('----------------------')
for i in range(2, 5):
    print(i)
    # 2, 3, 4
    # already in this, 2 is included, 5 not included and auto incremented.

print('----------------------')
for i in range (5, 2, -1):
    print(i)
    # 5, 4, 3
    # 5 included, 2 not included, decrement -1