"""
Cuidado com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutáveis)
"""
lista_a = ['Henrique', 'Maria']
lista_b = lista_a  # Atenção: as duas variáveis apontam para a mesma lista!

lista_a[0] = 'Qualquer coisa' # !!!!!
print(lista_b)

# Para ter duas listas separadas: 
lista_b = lista_a.copy() # duas listas diferentes
lista_a[0] = 'Henrique Bisetto' # alterando lista_a
print('Lista_a = ', lista_a)
print('Lista_b = ', lista_b) # lista_b permanece igual ao do momento da cópia


