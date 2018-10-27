#!/usr/bin/python3

var = 10

def escopo():
    global var
    var = 5
    print(var)

escopo()
print(var)

