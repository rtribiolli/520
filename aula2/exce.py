#!/usr/bin/python3
letras = ['a','b']
ling = {'daniel':'python'}
try:
    print(letras[2])
except IndexError as e:
    print('a lista contem apenas {} elementos'.format(
        len(letras)
    ))
    print(e)

print(ling.get('daniel'))