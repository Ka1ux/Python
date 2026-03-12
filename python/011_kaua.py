# 1 exrcicio
compra = 1000
taxa_juros = 0.02
meses = 5
valor_final = compra * (1 + taxa_juros) ** meses

print(f"Valor final da compra: R$ {valor_final:.2f}")

# 2 exrcicio

km = 10
hora = 1
velocidade_kmh = km / hora

velocidade_ms = velocidade_kmh * 1000 / 3600
print(f"Velocidade em m/s: {velocidade_ms:.2f} m/s")

velocidade_ms = velocidade_ms * 3600 / 1000
print(f"Velocidade em km/h: {velocidade_ms:.2f} km/h")

# 3 exrcicio

lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Média: {media:.2f}")

lista_min = lista[0]
lista_max = lista[0]

i = 0

for lista[i] in lista:
    if lista[i] > lista_min:
        lista_max = lista[i]
        i += 1
    else:
        lista_min = lista[i]
        i += 1

print(f"Valor mínimo: {lista_min}")
print(f"Valor máximo: {lista_max}")
