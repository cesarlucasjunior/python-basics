# Faça um programa que peça dois números e imprima o maior deles.

number_1 = int(input('Insira um número: '))
number_2 = int(input('Insira um segundo número: '))

if number_1 > number_2:
    print(number_1, 'foi o maior número inserido.')
else:
    print(number_2, 'foi o maior número inserido.')