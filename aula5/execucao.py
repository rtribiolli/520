from conta import Conta, Poupanca

c1 = Conta('Daniel', 12345, 1000)
c2 = Conta('Maria', 54321, 1000)

# c1.transferir(1100, c2)
# c2.render_juros()
# print(c1.saldo)
# print(c2.saldo)
c2.sacar(500)
print(c2.saldo)

c1.sacar(500)
print(c1.saldo)


