#!/usr/bin/python3

try:
    n = input('Digite um numero:')
    n = int(n)
    if n % 2 == 0:
        print('par')
    else:
        print('impar')

except ValueError:
    res = []
    for x in n:
        res.append(ord(x))
    res = sum(res)
    # res = [ord(x) for x in n]
    # res = sum(res)
    if res % 2 == 0:
        print('par {}'.format(res))
    else:
        print('impar {}'.format(res))

except Exception:
    print("Tratamento generico")

print('nao parei a execucao')