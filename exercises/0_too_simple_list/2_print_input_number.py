# Faça um programa que peça um número e então mostre a mensagem: "O número informado foi: [número]".

digito = input("Digite um número: ")

if digito.isdigit():
    print("O número informado foi:", digito)
else:
    print("O dígito inserido não é um número!")