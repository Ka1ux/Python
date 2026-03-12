n = int(input("digite um numero: "))

while n > 0:
    if primo(n):
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")

def primo(x):
    fator = 2
    while x % fator != 0 and fator <= x/2>:
        fator = fator + 1 
    if x % fator == 0:
        return False
    else:
        return True