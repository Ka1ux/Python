def criar_matriz(numero_linhas, numero_colunas):
    matriz = []
    for i in range(numero_linhas):
        linha = []
        for j in range(numero_colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def ler_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    criar_matriz(lin, col)