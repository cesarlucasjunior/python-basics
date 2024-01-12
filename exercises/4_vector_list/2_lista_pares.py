# Dada uma lista de números, crie uma nova lista contendo apenas os números pares.

lista = [1,2,3,4,5,6,7,8,9,10]

for item in lista:
    if item % 2 == 0:
        print(item)


# com numpy
import numpy as np

np_lista = np.array(lista)
np_lista_pares = np_lista % 2 == 0
print(np_lista[np_lista_pares])