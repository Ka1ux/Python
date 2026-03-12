# 1 exercicio
lista = [ "kaua barroso", "thiago felix", 
         "fernando henrique",
         "marcos vinicius", "gustavo alves"
]

normalized_list = [name.title() for name in lista] 
print(isinstance(normalized_list, list))  #Testezinho para verificar se normalized_list é uma lista
print(isinstance(normalized_list, normalized_list.__class__)) 
print(normalized_list)

# 2 exercicio
numero_telefone = input("Digite um número de telefone: ")
numero_telefone = numero_telefone.replace(" ", "")
if numero_telefone.startswith("+55"):
    numero_telefone = numero_telefone[3:]

print(numero_telefone)

ddd = numero_telefone[0:2]
parte1 = numero_telefone[2:7]
parte2 = numero_telefone[7:11]

numero_telefone = f"({ddd}) {parte1}-{parte2}"
print(numero_telefone)

# 3 exercicio
titulo = input("Digite um titulo: ")

titulo_slug = titulo.lower().replace(" ", "-")
print(titulo_slug)

#3 exercicio com chat gpt --------------------------
import unicodedata

titulo = input("Digite um titulo: ")

titulo_sem_acentos = "".join(
    c for c in unicodedata.normalize("NFD", titulo)
    if unicodedata.category(c) != "Mn"
)

titulo_slug = titulo_sem_acentos.lower().replace(" ", "-")
print(titulo_slug)
