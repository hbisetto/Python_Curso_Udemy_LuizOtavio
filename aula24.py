# Operadores in e not in
# Strings são iteráveis (conta um caractere por vez)
#  0 1 2 3 4 5 6 7  
#  H e n r i q u e
# -8-7-6-5-4-3-2-1

#nome = 'Henrique'
#print(nome[2])
#print('à' in nome)
#print(10 * '-')
#print('è' not in nome)

nome = input('Digite seu nome: ')
encontrar = input ('Digite o que deseja encontrar')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    

