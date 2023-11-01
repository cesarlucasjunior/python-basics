# Faça um programa que converta metros para centímetros.

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


print("Esse sistema converte metros para centímetros!")

valor_em_metros = input("Digite uma valor em metros:")

if not isfloat(valor_em_metros):
    print("O valor em metros precisa ser um número!")
else:
    valor_em_centimetros = float(valor_em_metros) * 100
    print("A conversão dá ", valor_em_centimetros, " cm")
