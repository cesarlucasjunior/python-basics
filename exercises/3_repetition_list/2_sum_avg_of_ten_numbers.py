print("Esse programa pega 10 número e calcula a soma, a média e retorna quantos número foram ímpares")

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    



def isOdd(value):
   return value % 2 == 1

sum = 0
odds = 0
n = 0

while n < 10:
    numero = input("Digite um número: ")
    if(not isfloat(numero)):
        print("Todo os dígitos precisam ser números!")
        break
    else: 
        sum += float(numero)
        if isOdd(float(numero)):
            odds +=1
        n+=1

print(f"A soma total deu {sum:.2f}")
print(f"A média é de {sum/10:.2f}")
print(f"A quantidade de ímpares é {odds}")

