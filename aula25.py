""" 
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal 

"""

nome = 'Henrique'
preco = 1293.12939123
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)

print('O hexadecimal de %d é %x' % (17, 17))