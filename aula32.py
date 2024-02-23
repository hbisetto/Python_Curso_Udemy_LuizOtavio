"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print('Exercícios da aula 32')

# Exercício 1
print('Exercício 1: ')
# mensagem_1 = ('Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número \
# inteiro, informe que não é um número inteiro.')
# print(mensagem_1)

num_str = input('Digite um número inteiro: ')
checagem = num_str.isdigit()

# print(checagem)

if checagem: 
    num_int = int(num_str)
    par = (num_int % 2) == 0
    if par:
        print(f'O número {num_int} é par.')
    else:
        print(f'O número {num_int} é ímpar.')
else:
    print('O número digitado não é um número inteiro')
 
# Exercício 2    

hora_str = input('Digite a hora: ')
hora_int = int(hora_str)

manha = hora_int >= 0 and hora_int <=11
tarde = hora_int >=12 and hora_int <= 17

if manha:
    print('Bom dia')
elif tarde:
    print('Boa tarde')
else: 
    print('Boa noite')

# Exercício 3
    
nome = input('Digite o seu primeiro nome: ')
tamanho = len(nome)
tamanho_medio = tamanho == 5 or tamanho == 6

if tamanho <= 4:
    print('Você tem um nome pequeno')
elif tamanho_medio:
    print('Você tem um nome normal')
elif tamanho > 6:
    print('Você tem um nome grande')
else:
    print(f'{nome} é inválido')

