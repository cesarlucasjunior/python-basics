import numpy as np
np_array1 = np.array([1,2,3,4,5])
np_array2 = np.array([6,7,8,9,10])

np_array_duas_dimensoes = np.array([np_array1, np_array2])
print(np_array_duas_dimensoes)
print(type(np_array_duas_dimensoes))
print(np_array_duas_dimensoes.shape)

#subsetting
print('------SUBSETTING------')
print(np_array1[2])
print(np_array_duas_dimensoes[0][2])
print(np_array_duas_dimensoes[0,2])
print(np_array_duas_dimensoes[0][:6])
print(np_array_duas_dimensoes[1,:])