# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

digito = input('Digite uma letra: ')
digito = digito.lower()

if (digito == 'a' or digito == 'e' or
   digito == 'i' or digito == 'o' or digito == 'u'):
    print('A letra digitada é uma vogal.')
else:
    print('A letra digitada é uma consoante.')