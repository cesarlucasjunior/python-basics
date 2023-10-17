# Faça um programa que leia três números e mostre o maior deles.

number_1 = int(input('Insira o primeiro número: '))
number_2 = int(input('Insira o segundo número: '))
number_3 = int(input('Insira o terceiro número: '))

if(number_1 > number_2) and (number_1 > number_3):
    print('O primeiro número digitado foi o maior entre os três!')
elif(number_2 > number_3) and (number_2 > number_1):
    print('O segundo número digitado foi o maior entre os três!')
else:
    print('O terceiro número digitado foi o maior entre os três!')
