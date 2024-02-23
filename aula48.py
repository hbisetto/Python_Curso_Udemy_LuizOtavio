""" 
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#.........01234
#........-54321
string = 'ABCDE' # 5 caracteres (len)
# lista = list()
#........0.....1.....2...................3...4
lista = [123, True, 'Henrique Bisetto', 1.2, []]
# print(lista, type(lista))
# print(bool([])) # falsy
print(lista[0])
print(lista[1])
print(lista[2].upper())
print(lista[3], 'do tipo: ', type(lista[3]))
print(lista[4])
print(lista)
# Alterando valores da lista:
lista[2] = 'Maria'
print(lista)
print(lista[2])
