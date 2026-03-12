def MinMax(temperaturas):
    print("A menor temperatura é: ", min(temperaturas))
    print("A maior temperatura é: ", max(temperaturas))


def min(temps):
    i = 1
    min = temps[0]
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def max(temps):
    i = 1
    max = temps[0]
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

