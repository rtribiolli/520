#!/usr/bin/python3

def ler_arquivo(nome):
    """ 
    funcao para ler arquivo 
    -> str nome do arquivo
    return -> list conteudo do arquivo
    """
    with open(nome , 'r') as arq:
        return arq.readlines()
    

def escrever_arquivo(nome, conteudo):
    with open(nome, 'w') as arq:
        arq.write(conteudo + '\n')

if __name__ == '__main__':
    print('hello')