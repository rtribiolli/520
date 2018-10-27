#!/usr/bin/python3

#testar com diciionario
convidados = []

def adicionar(nome, idade):
    """ funcao para adicionar convidados na lista """
    global convidados
    convidados.append(nome, idade)
    return True

while True:
    nome = input("nome ou sair: ")
    if nome.strip().lower() == 'sair':
        break
    idade = int(input('Digite a idade: '))
    adicionar(nome, idade)

print (convidados)