# Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

from isfloat import isfloat
import math

print("Esse programa calcula a área de um círculo")

raio_circulo = input("Informe o raio do circulo: ")

if not isfloat(raio_circulo):
    print("O raio do círculo precisa ser um número!")
else: 
    area = math.pi * (float(raio_circulo) ** 2)
    print(f"A área do círculo com raio {raio_circulo} é {area:.2f}")