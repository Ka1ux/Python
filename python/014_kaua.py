# 1 exercício
peso = float(input("Digite o peso do peixe: "))
altura = float(input("Digite a altura do peixe: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")

#2 exercício
consumo = float(input("Digite o consumo de energia em kWh: "))
tarifa = input("Digite a tarifa de energia em R$: ")
valor = consumo * tarifa
print("O valor a ser pago é: R$ ", valor)

#3 exercício
data = input("Digite a data no formato DD/MM/AAAA: ")
dia, mes, ano = data.split("/")
print("Dia: ", dia)
print("Mês: ", mes)
print("Ano: ", ano)
