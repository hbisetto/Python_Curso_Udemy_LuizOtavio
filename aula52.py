""" 
Tipo tupla - Uma lista imutável
""" 

nomes = 'Henrique', 'Helga', 'Thales'
print(nomes)
print(type(nomes))
print(nomes[0])
nomes_tupla = tuple(nomes)
nomes_lista = list(nomes_tupla)
print('Esta é uma tupla: ', nomes)
print('Esta é uma lista: ', nomes_lista)
print('Esta é uma tupla: ', nomes_tupla)
