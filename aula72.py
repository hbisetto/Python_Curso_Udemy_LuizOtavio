# Exercícios com funções

# Crie um função que multiplic todos os argumentos 
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.abs

# 1)
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
        
    return total

x = multiplica(2, 3, 4)
print(x)

def par_impar(x):
    if (int(x) % 2) == 0:
        print(f'{x} é um número par.')
    else:
        print(f'{x} é um número ímpar')
        
par_impar(2)
par_impar(3)