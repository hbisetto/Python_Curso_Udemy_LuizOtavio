""" 
Imprecisão de ponto flutuante

"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print('Print para ressaltar o problema')
print(numero_3)

print('Resultado com f string')
print(f'{numero_3:.2f}') # Exibir como string formatada

print('Print com a função round()')
print(round(numero_3, 2))   # float com a 'correção' de valores

numero__1 = decimal.Decimal(0.1) # Para cálculos mais específicos, precisos
numero__2 = decimal.Decimal(0.7)
numero__3 = numero__1 + numero__2
print('Resultado com import decimal decimal.Decimal()')
print(numero__3)

num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')
num3 = num1 + num2
print('Resultado com import decimal passando parâmetro entre aspas')
print(num3)
