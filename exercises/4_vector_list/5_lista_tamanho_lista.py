# Dada uma lista de palavras, crie uma nova lista contendo o comprimento de cada palavra.

lista = ['Joana', 'Pedro', 'Wesley', 'Márcio', 'Judite', 'Aline', 'Ana']
lista_size = []

for item in lista:
    size = len(item)
    lista_size.append(size)

print(lista_size)
