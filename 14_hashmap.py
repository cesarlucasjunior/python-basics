# hashmap or dictionary are data structures that work with key:value and dont allowed 
# duplicated keys.

# a chave do hashmap é essencial para as operações do dicionário.

# declaring a hashmap:
myhashmap = {}

# assignment:
myhashmap['ana'] = 18
myhashmap['john'] = 22
myhashmap['paul'] = 23
# myhashmap['ana'] = 24

print(myhashmap)
print(len(myhashmap))

# reassignment:
myhashmap['ana'] = 19
print(myhashmap)

# validating existence of a key:
print('ana' in myhashmap)

# another way to declare and assign a hashmap:
myotherhashmap = {'ana': 19, 'john': 22, 'paul': 23}
print(myotherhashmap)

# another way is via dict comprehension:
hashmapp = {i: i+1 for i in range(5)}
print(hashmapp)

# looping through hashmap:
for key in myhashmap:
    print(key, '-', myhashmap[key])

print('------------------------')

for val in myhashmap.values():
    print(val)

print('------------------------')

for key, value in myhashmap.items():
    print(key, '-', value)