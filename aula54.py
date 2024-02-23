""" 
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os
opcao = ''
opcoes = ('i', 'a', 'l')
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opcao.lower() == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    
    elif opcao.lower() == 'a':
        try:
            indice = int(input('Escolha o índice para apagar: '))
            if indice > len(lista):
                print('Não foi possível apagar esse índice.')
            else:
                del lista[indice]        
        except:
            print('Não foi possível apagar este índice')
            
    elif opcao.lower() == 'l':
        os.system('cls')
        enumeracao = enumerate(lista)
        for num, item in enumeracao:
            print(num, item)
            
    elif opcao.lower() == 's':
        break
            
    else:
        print('Opção inválida. Tente novamente.')
        continue
    