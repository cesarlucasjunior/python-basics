# Dada uma lista de números, encontre o maior e o menor valor:
import math
lista = [7, 23, 12, 44, 30, 88, 3]
maior = 0
menor = 1000

for item in lista:
    if item > maior:
        maior = item
    
    if item < menor:
        menor = item

print(f'Maior: {maior}')
print(f'Menor: {menor}')


# Ou:

maior_facil = max(lista)
menor_facil = min(lista)
print('-------------------')
print(f'Maior: {maior_facil}')
print(f'Menor: {menor_facil}')