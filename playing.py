# Crie uma lista com vários elementos de tipos diferentes.
# Adicione na lista mais um elemento, exluindo-o em seguida.
# Defina a complexidade algorítmica de cada ação.
# Insira um novo elemento na terceira posição e reatribua seu valor.
# Explique a complexidade de cada ação.
# Imprima o tamanho do array.
# Imprima os dois últimos elementos do array.

array = [0, 0.9, "Paula", True]

array.append(False)
print(array) #O(1)

array.pop()
print(array) #O(1)

#stack

array.insert(3, False)
print(array) #O(n)

array[3] = True
print(array) #O(1)