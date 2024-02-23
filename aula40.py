"""
Calculadora com while
"""

while True: 
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador [+, -, *, /]: ')

    print(f'Operação = {num_1} {operador} {num_2}')
    
    if operador == '+':
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        resultado = num_1_float + num_2_float
        print('O resultado é ', resultado)
    elif operador == '-':
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        resultado = num_1_float - num_2_float
        print('O resultado é ', resultado)
    elif operador == '*':
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        resultado = num_1_float * num_2_float
        print('O resultado é ', resultado)
    elif operador == '/':
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        resultado = num_1_float / num_2_float
        print('O resultado é ', resultado)
    
    questao = input('Para [s] para sair ')
    questao = questao.lower() 
    questao = questao.startswith('s')
    
    if questao :
        break



