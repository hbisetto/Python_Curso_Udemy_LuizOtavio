frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'
    
# print(frase.count('Python'))

i = 0
qtde_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    qtde_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if qtde_apareceu_mais_vezes < qtde_apareceu_mais_vezes_atual:
        qtde_apareceu_mais_vezes = qtde_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
        
#    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1
    
print(
    'A letra que apareceu mais vezes foi "'
    f'{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtde_apareceu_mais_vezes}x'
)
    
    