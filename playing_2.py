# Crie uma variável com elementos de 1 a 10
# Crie uma sublista de lista com os 5 primeiros elementos
# Para cada elemento do array, jogue para uma variável

lista = [i for i in range(1, 11)] #list comprehension
print(lista)

sublista = lista[:5] #slicing
print(sublista)

a, b, c, d, e = sublista #unpacking
print(f'A - {a}, B - {b}, C - {c}, D - {d}, E - {e}')

# Percorra cada elemento da lista - com elemento, com índice, com índice e elemento

for elemento in lista:
    print(f'{elemento}')

for indice in range(len(lista)):
    print(f'{lista[indice]}')

for indice, elemento in enumerate(lista):
    print(f'{indice} - {elemento}')