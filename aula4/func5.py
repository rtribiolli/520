#!/usr/bin/python3

def parametros(**kwargs):
    print(kwargs['nome'])

parametros(nome='daniel', idade=24)
# def parametro(*args):
#     print(args)
#     for x in nome:
#         print(x)

# parametro('daniel', 'maria', 5, [], {})
