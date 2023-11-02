n = 0
total = 0

while n < 10:
    numero = input("Digite um numero: ")
    total += int(numero)
    n += 1

print(f"A soma total das leituras é {total:.2f}")