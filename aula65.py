"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def imprimir(a, b, c):
    print(a, b, c)

a = 'aaa'
b = 'bbb'
c = 'ccc'

imprimir(a, b, c)
imprimir(1, 2, 3)
imprimir('Paralelepípedo', 'Telescópio', 'Zaratrusta')
imprimir(True, True, False)

def saudacao(nome='Sem nome'): # se não passar parâmetro, vai o 'Sem nome'
    print(f'Olá, {nome}!')

saudacao('Henrique Bisetto')
saudacao() # sem parâmetro