#1 exercicio
preco_1 = 10
preco_2 = 20
qnt_1 = 2
qnt_2 = 3
total_1 = preco_1 * qnt_1
total_2 = preco_2 * qnt_2

if total_1 > total_2:
    print("Produto 1 é mais caro")
elif total_1 < total_2:
    print("Produto 2 é mais caro")
else:
    print("Os produtos têm o mesmo preço")

#2 exercicio
brinquedo_altura = 1.5
brinquedo_idade = 15


altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))

if altura >= brinquedo_altura and idade >= brinquedo_idade:
    print("Você pode brincar no brinquedo.")
else:
    print("Você não pode brincar no brinquedo.")

#exercicio 3
idade = int(input("Digite sua idade: "))
if idade > 18:
    print("Você pode acessar areas restritas.")
else:
    print("Você é menor de idade, não pode acessar areas restritas.")