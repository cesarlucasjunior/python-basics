# Crie uma variável com elementos de 1 a 10
# Crie uma sublista de lista com os 5 primeiros elementos
# Para cada elemento do array, jogue para uma variável

lista = [i for i in range(1,11)] #list comprehension
print(f'Lista criada - {lista}')

sublista = lista[:5] #slicing
print(f'Sublista - {sublista}')

a, b, c, d, e = sublista #unpacking
print(f'A - {a}, B - {b}, C - {c}, D - {d}, E - {e}')


# Percorra cada elemento da lista

for elemento in lista:
    print(f'Elemento - {elemento}')

for indice in range(len(lista)):
    print(f'Índice {indice} - {lista[indice]}')

for indice, elemento in enumerate(lista):
    print(f'{indice} - {elemento}')


