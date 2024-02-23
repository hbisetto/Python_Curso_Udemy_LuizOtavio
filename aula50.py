""" 
Exercício
Exiba os índices da lista

"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
lista.append('Maria')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    
