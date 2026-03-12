#1 exercicio
preco_item = float(input("Digite o preço do item: "))
valor_pago = float(input("Digite o valor pago: "))

troco = valor_pago - preco_item
print(f"O troco a ser devolvido é: R$ {troco:.2f}")

#2 exercicio
km_percorrido = float(input("Digite a distância percorrida em km: "))
litros_consumidos = float(input("Digite a quantidade de litros consumidos: "))
consumo_medio = km_percorrido / litros_consumidos
print(f"O consumo médio do veículo é: {consumo_medio:.2f} km/l")

#3 exercicio
taxa = float(input("Digite a taxa de juros mensal (em %): "))
boleto_atrasado = float(input("Digite o valor do boleto atrasado: "))
dias = int(input("Digite o número de dias de atraso: "))

juros = boleto_atrasado * (taxa / 100) * (dias / 30)
valor_total = boleto_atrasado + juros
print(f"O valor total a ser pago é: R$ {valor_total:.2f}")