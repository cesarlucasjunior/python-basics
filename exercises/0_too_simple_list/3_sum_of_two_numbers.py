# Faça um programa que peça dois números e imprima a soma.

print("Esse programa soma dois número", end="\n")
numero_1 = input("Insira o primeiro número:")
numero_2 = input("Insira o segundo número:")

if(not numero_1.isdigit() or not numero_2.isdigit()):
    print("Os dígitos precisam ser números!")
else:
    print(int(numero_1) + int(numero_2))