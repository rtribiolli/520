#!/usr/bin/python3

quadrados = []
for x in range(1,11):
    quadrados.append((lambda y: y **2)(x))

print (quadrados)
quadrados = [x ** 2 for x in range(1,11)]

quadrados = list(map(lambda x: x **2, range(1,11))
map()
# a = lambda x , y : x + y
# print(a(2,5))

# print((lambda x, y : x + y)(3, 3))
# lambda x : x.title()
