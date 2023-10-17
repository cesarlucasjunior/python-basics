# Faça um programa que verifique se uma letra digitada é F ou M. Conforme a letra, retorne:
# F - Feminino, M - Masculino, Sexo inválido.

sexo = input('Digite seu sexo - Feminino (F) ou Masculino (M): ')

if (sexo == 'M' or sexo == 'm'):
    print('M - Masculino')
elif sexo == 'F' or sexo == 'f':
    print('F - Feminino')
else:
    print('Sexo inválido')