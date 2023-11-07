# Cria uma lista com list comprehension:
lista = [i for i in range(1, 10)]
print(lista)

outra_lista = [lista + 1 for lista in range(1,10)]
print(outra_lista)

list_2d = [[i]*i for i in range(1,10)]
print(list_2d)