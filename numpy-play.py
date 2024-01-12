import numpy as np

altura = [1.69, 1.70, 1.81, 1.81, 1.73]
peso = [75, 70, 76, 77, 79]

np_altura = np.array(altura)
np_peso = np.array(peso)

bmi = np_peso / (np_altura * np_altura)

print(bmi)
print(type(bmi))

#x = [15,10,2,84] + [1,4,8,7,9]
#print(x.index(x.count(x[0])))

#count() - conta o número de vezes que um determinado elemento aparece numa lista, retornando-o.
#index() - retorna o índice de um determinado elemento dentro de uma lista.



