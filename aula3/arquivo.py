#!/usr/bin/python3

# arq = open('teste.txt', 'r')
# print(arq.read())
# arq.close()

with open('teste.txt', 'r') as arq:
    #arq.seek(0)
    print(arq.read(), end='')
    # print(arq.readline(), end='')
    # print(arq.tell())
    # print(arq.readline(), end='')
