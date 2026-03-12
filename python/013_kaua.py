# 1 exercicio
compra = float(input("Digite o valor da compra: "))

if compra >= 150:   
    print("Frete gratis")
    frete = 0
else:
    print("Frete normal")
    frete = 20

# 2 exrcicio
quant = int(input("Quantos numeros você quer digitar? "))
numeros = []

for i in range(quant):
    n = int(input("Digite um numero: "))
    numeros.append(n)


soma = sum(numeros)
media = soma / len(numeros)
print("A média é:", media)

if media > 3:
    print("aprovado")
else:
    print("reprovado")

# 3 exercicio

quant = int(input("digite 2 numeros inteiros:"))
numeros = []

for i in range(quant):
    n = int(input("Digite um numero: "))
    numeros.append(n) 

if numeros[0] > numeros[1]:
    print("O maior numero é:", numeros[0])
elif numeros[1] > numeros[0]:
    print("O maior numero é:", numeros[1])
else:
    print("Os numeros são iguais.")