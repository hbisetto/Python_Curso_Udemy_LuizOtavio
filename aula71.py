""" 
args - Argum ents não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembrete de desempacotamento

# x, y, *resto = 1, 2, 3, 5
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    
x = soma(1, 2, 3, 4, 5, 6, 7)
print(x)

# funcao sum()

numeros = 1, 2, 3, 4
print(numeros)
print(*numeros)
print(sum(numeros))