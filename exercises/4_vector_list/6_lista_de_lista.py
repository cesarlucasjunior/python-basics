# Crie duas listas de números e crie uma terceira lista que contenha a soma dos elementos correspondentes das duas listas.

lista_1 = [1,2,3,4,5,6,7,8,9]
lista_2 = [9,8,7,6,5,4,3,2,1]

lista_3 = []


for i in range(len(lista_1)):
    lista_3.append(lista_1[i]+lista_2[i])

print(lista_3)

# Com numpy:
import numpy as np

np_lista_1 = np.array(lista_1)
np_lista_2 = np.array(lista_2)

np_lista_3 = np_lista_1 + np_lista_2
print(np_lista_3)