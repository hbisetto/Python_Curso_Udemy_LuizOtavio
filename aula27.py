"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[5])
print(variavel[4:]) # a partir do caractere 4 até o fim
print(variavel[4:8])
print(variavel[0:5]) # o 5 não é incluído
print(len(variavel))
print(len(variavel[4]))
print(len(variavel[4:6]))
print(variavel[-1:-10:-1]) # vai de 0 9 na contagem invertida