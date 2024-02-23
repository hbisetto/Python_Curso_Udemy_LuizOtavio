primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'Os valores {primeiro_valor=} e {segundo_valor=} são iguais')
else:
    print(f'Os valores {primeiro_valor=} e {segundo_valor=} são inválidos')    