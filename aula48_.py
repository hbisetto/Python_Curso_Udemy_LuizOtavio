""" 
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
CRUD
"""
lista = [1, 2, 3, 4]
# print(lista[2]) # 3
# numero = lista[2]
# print(numero)
lista[2] = 300
del lista[2] # 3 foi apagado
print(lista)
print(lista[2]) # o índice 2 é = 4 agora, pois o 300 foi apagado acima

lista.append(5) # adiciona elementos no final
lista.append(6)
lista.append(7)
# a lista atualizada: [1, 2, 4, 5, 6, 7]
print(lista)
lista.pop() # apaga o último elemento da lista
# lista atualizada: [1, 2, 4, 5, 6]
print(lista)
ultimo_valor = lista.pop() # 1) removeu 6 da lista e o retornou na variável
print(lista, 'Removido ', ultimo_valor)

# Métodos úteis:
print(40 * '*')
print('MÉTODOS ÚTEIS:')
print()
lista.clear()
lista = [10, 20, 30, 40]
lista.append('Henrique')
nome = lista.pop()
print(lista)
print(nome)
print(lista, nome)
lista.append(1234)
lista.append(5678)
del lista[-1]
print(lista)
lista.insert(0, 5) # 0 é o índice que será add e 5 é o valor
print(lista)
print('len = ', len(lista))

print(40 * '*')
print()

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # estende a lista a ficando a + b
print(lista_a)

