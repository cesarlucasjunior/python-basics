# Faça um programa que peça as quatro notas bimestrais e mostre a média.


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



print("Esse programa te trará a média das suas notas no ano!", end="\n")

nota_1_bimestre = input("Sua nota no primeiro bimestre: ")
nota_2_bimestre = input("Sua nota no segundo bimestre: ")
nota_3_bimestre = input("Sua nota no terceiro bimestre: ")
nota_4_bimestre = input("Sua nota no quarto bimestre: ")


if(not isfloat(nota_1_bimestre) or
   not isfloat(nota_2_bimestre) or
   not isfloat(nota_3_bimestre) or
   not isfloat(nota_4_bimestre)):
    print("As notas precisam ser numeros")
else:
    soma_total = float(nota_1_bimestre) + float(nota_2_bimestre) + float(nota_3_bimestre) + float(nota_4_bimestre)
    media = soma_total/4
    print("A média do ano é ", media)