#!/usr/bin/python3

ling = input("qual a melhor linguagem de programacao?")
ling = ling.strip().lower()
try:
    if ling == 'python':
        print('voce esta no caminho certo')
    elif ling == 'html' or ling == 'css':
        raise ValueError('isso nao e linguagem de programacao')
    else:
        print('Mude pra python!')
except ValueError as e:
    print(e)

exit()



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