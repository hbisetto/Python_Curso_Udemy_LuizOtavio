""" 
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# Explicação detalhada de como funciona o for

# texto = iter('Henrique') # __iter__()

# print(texto.__next__()) # H
# print(texto.__next__()) # e
# print(texto.__next__()) # n 
# print(next(texto))      # r pois é o mesmo comando

texto = 'Henrique Bisetto' # iterável
# iterador = iter(texto) # iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)