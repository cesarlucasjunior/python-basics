# Crie uma lista com vários elementos de tipos diferentes.
# Adicione na lista mais um elemento, exluindo-o em seguida.
# Defina a complexidade algorítmica de cada ação.
# Insira um novo elemento na terceira posição e reatribua seu valor.
# Explique a complexidade de cada ação.
# Imprima o tamanho do array.
# Imprima os dois últimos elementos do array.

lista = [3, 3.33, 'Ana', True]

lista.append(False)
print(f'Lista com novo item - {lista}') #O(1)

lista.pop()
print(f'Lista com item removido - {lista}') #O(1)

lista.insert(3, False)
print(lista) #O(n)

lista[3] = True
print(lista) #O(1)
lista[3] = False

print(f'O tamanho do array é de {len(lista)} elementos')
print(f'O penúltimo elemento do array é {lista[-2]}')
print(f'O último elemento do array é {lista[-1]}')