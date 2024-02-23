"""
Iterando strings com while
"""
#       0123456789......
nome = 'Henrique Bisetto' # Iteráveis

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

contador = 0
nova_str = ''

while contador < tamanho_nome:
    nova_str += (f'*{nome[contador]}')
    contador += 1

print(nova_str)