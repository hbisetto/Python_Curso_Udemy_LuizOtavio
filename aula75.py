# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#    return numero * 2

# def triplicar(numero):
#    return numero * 3

# def quadruplicar(numero):
#    return numero * 4

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))


def multiplicar(por):
    def operacao(numero):
        return numero * por
    return operacao

por_dois = multiplicar(2)
por_tres = multiplicar(3)
por_quatro = multiplicar(4)
por_duzentos = multiplicar(200)

print(por_dois(15))
print(por_duzentos(5))