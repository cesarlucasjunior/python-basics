# Crie uma lista de nomes e ordene-a em ordem alfabética. Em seguida, inverta a ordem da lista.

lista = ['Ana', 'Marcela', 'João', 'Joaquina', 'Priscila', 'Marcos', 'Nathan']

lista_ordenada = sorted(lista)
print(lista_ordenada)
reversed_list = lista_ordenada.copy()
reversed_list.reverse()
print(reversed_list)