class carro:
    pass
meu_carro = carro()
meu_carro.cor = "vermelho"
meu_carro.modelo = "Fusca"
meu_carro.ano = 1980

carro_vizinho = carro()
carro_vizinho.cor = "azul"
carro_vizinho.modelo = "Gol"
carro_vizinho.ano = 2010

print("Meu carro é um {} {} de {}".format(meu_carro.cor, meu_carro.modelo, meu_carro.ano))

print("O carro do meu vizinho é um {} {} de {}".format(carro_vizinho.cor, carro_vizinho.modelo, carro_vizinho.ano))

class carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

meu_carro = carro("vermelho", "Fusca", 1980)
carro_vizinho = carro("azul", "Gol", 2010) 



class carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.velocidade = 0
        self.velocidade_maxima = vm

def imprimar(self):
    if self.velocidade == 0:
        print(" %s %s de %d está parado." % (self.cor, self.modelo, self.ano))
    elif self.velocidade < self.velocidade_maxima:
        print(" %s %s de %d está a %d km/h." % (self.cor, self.modelo, self.ano, self.velocidade))
    else:
        print(" %s %s de %d está a velocidade máxima de %d km/h." % (self.cor, self.modelo, self.ano, self.velocidade_maxima))

def acelerar(self, incremento):
    self.velocidade = incremento
    if self.velocidade > self.velocidade_maxima:
        self.velocidade = self.velocidade_maxima
    self.imprimar()

def frear(self, decremento):
    self.velocidade = decremento
    if self.velocidade < 0:
        self.velocidade = 0
    self.imprimar()