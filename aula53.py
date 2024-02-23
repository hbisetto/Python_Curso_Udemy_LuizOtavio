""" 
enumerate - enumera iteráveis (índices)
""" 

lista  = ['Maria', 'João', 'Carlos']
lista.append('Henrique')

# lista_enumerada = enumerate(lista)
# prit(lista_enumerada)
# print(next(lista_enumerada))
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

for indice, nome in enumerate(lista): # item estava onde está indice e nome
#    indice, nome = item
    print(indice, nome)
    
# for item in enumerate(lista):
#     for valor in item:
#         print(valor)
