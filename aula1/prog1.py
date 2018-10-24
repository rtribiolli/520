#!/usr/bin/python3

idade = int(input('idade:'))
if idade >= 18:
    print('entra')
else:
    acompanhado = input('acompanhado dos pais sim ou nao: ')
    if acompanhado == "sim":
        print('entra')
    else:
        print('nao entra')
