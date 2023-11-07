nums = [i for i in range(1, 100)]
tamanholote = 50
lote = [nums[i:i+tamanholote] for i in range(0, len(nums), tamanholote)]
#slicing de uma lista gera uma nova lista
#print(nums[0:0+50])
#print(nums[50:50+50])
print(lote)