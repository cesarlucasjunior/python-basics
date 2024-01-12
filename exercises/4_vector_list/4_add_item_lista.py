# Crie uma lista de tarefas a fazer. Adicione, remova e marque tarefas como concluídas.

lista = []

lista.append('Iogurte')
lista.append('Macarrão')
lista.append('Carne')
lista.append('Tomate')
lista.append('Alface')

#ordenando
lista_ordenada = sorted(lista)
print(lista_ordenada)

lista_ordenada.remove('Tomate')
print(lista_ordenada)

#reversing
lista_ordenada.reverse()
print(lista_ordenada)