class Carro:
    def __int__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f"O carro {self.nome} está acelerando!")

fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()

celta = Carro("Celta")
print(celta.nome)
celta.acelerar()