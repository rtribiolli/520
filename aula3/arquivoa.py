#!/usr/bin/python3
# lista = ['a', 'b', 'c']
with open('teste.txt', 'a') as arq:
    conteudo = arq.readlines()

print(conteudo)

with open('teste.txt', 'w') as arq:
    arq.writelines(conteudo)
    
    # for x in lista:
    #     arq.write('{}\n'.format(x))
    
    #arq.write(lista)
   # arq.write('estou escrevendo lero lero\n')

