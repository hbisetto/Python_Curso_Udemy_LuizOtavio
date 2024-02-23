"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'henrique bisetto'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC'  não vai funcionar pois o dado é imutável
print(string)
print(outra_variavel)

# usando um método na string
print(string.capitalize()) # primeira letra maiúscula
print(string.zfill(100))