# hashset are data structures that no allow duplicate items. 
# his search and insert values in constant time.

# como só podemos ter um valor, nunca repetido, esse valor é como uma chave para as operações
# do hashset.

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(3)
myset.add(3)

print(myset)
print(len(myset))
print(3 in myset)

myset.add(33)
print(myset)
myset.remove(33)
print(myset)

# another way to declare a set:
print(set([12,21,33]))

# declaring set via comprehension:
myset = {i for i in range(3)}
print(myset)