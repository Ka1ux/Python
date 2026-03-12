# 1 exercicio
name = input("Enter your name: ")
age = input("enter your age: ")
city = input("enter your city: ")
on = input("enter if you on:")

print("Your name is " + name + ", you are " + str(age) + "years old, you live in " + city + " and you are " + on)

# 2 exercicio

preco_antigo = 10
preco_novo = preco_antigo

# 3 exercicio

preco = 10

TAXA_SERVICO = 0.1
DESCONTO = 0.2
precom_com_taxa_e_desconto = preco * (1 + TAXA_SERVICO) * (1 - DESCONTO)
print("O preço final é: " + str(precom_com_taxa_e_desconto))
