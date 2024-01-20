import numpy as np 

# rie um array 1D com 5 elementos inteiros.
np_1d = np.array([1,2,3,4,5])

# Crie uma matriz 2D (3x3) com números inteiros.
np_2d = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

# Crie um array de zeros com 4 elementos.
np_4_0 = np.array([0 for i in range (4)])

# Crie uma matriz de uns (5x5).
np_5_5 = np.array([[i for i in range(5)] for i in range(5)])

print(np_1d.shape)
print(np_2d.shape)
print(np_4_0)
print(np_5_5)