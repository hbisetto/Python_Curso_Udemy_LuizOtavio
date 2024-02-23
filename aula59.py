# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena', ], # 0
    ['Elaine', ], # 1
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print(*lista)
# print(*string)
# print(*tupla)
print(*salas, sep='\n')
