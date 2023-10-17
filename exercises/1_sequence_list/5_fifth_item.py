# Faça um programa que pergunte o preço de três produtos e informe qual produto deve ser comprado,
# sabendo que a decisão é sempre pelo mais barato.

preco_produto_1 = int(input('Digite o preço do primeiro produto: '))
preco_produto_2 = int(input('Digite o preço do segundo produto: '))
preco_produto_3 = int(input('Digite o preço do terceiro produto: '))

if(preco_produto_1 == preco_produto_2 == preco_produto_3):
    print('O preço é igual, compre qualquer um!')
elif(preco_produto_1 < preco_produto_2) and (preco_produto_1 < preco_produto_3):
    print('Compre o primeiro produto!')
elif(preco_produto_2 < preco_produto_3) and (preco_produto_2 < preco_produto_1):
    print('Compre o segundo produto!')
else:
    print('Compre o terceiro produto!')