nums = [i for i in range(100)]
tamanholote = 50
lote = [nums[i:i+tamanholote] for i in range(0, len(nums), tamanholote)]

#print(lote)

lista = [i for i in range(0, 51, 10)]
print(lista)

# 1 - de onde começa
# 2 - até onde vai (não inclusivo)
# 3 - incremento, de quantos em quantos