#!/usr/bin/python3

cria = input("nome do arquivo: ")
shebang = "#!/usr/bin/python\n"
try:
    with open('cria', 'x') as arq:
        arq.write(shebang)

except FileExistsError:
    with open('cria', 'r') as arq:
        conteudo = arq.readlines()
    if conteudo:
        if conteudo[0] != shebang:
            conteudo.insert(0, shebang)

        with open(cria, 'w') as arq:
            arq.writelines(conteudo)
    else:
        with open(cria, 'a') as arq:
            arq.write(conteudo)
   # print('v ' if conteudo[0] == shebang else 'f')


    # conteudo.insert(0, shebang)
    #     arq.seek(0)
    #     arq.write("#!/usr/bin/python\n")

#!/usr/bin/python\n#!/usr/bin/python\n