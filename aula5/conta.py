'''titular numero da conta e saldo
metodos= depositar, sacar, trasnferir'''

class Conta():
    '''tentando abstrair uma conta corrente'''
    def __init__(self,titular,num,saldo=0):
        self.titular = titular
        self.numero = num
        self.saldo = saldo
        self.taxa = 0.5

    def depositar(self, valor):
        self.saldo+=valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo-= (valor + self.taxa)
            return "saque realizado com sucesso"
        else:
            raise ValueError ("Saldo insuficiente {}".format(self.saldo))
        
    def transferir(self, valor, conta):
        try:    
            self.sacar(valor)
            conta.depositar(valor)
            return "transferencia ok"
        except ValueError as e:
            print(e)
            return 'nao foi possivel realizar a transferencia'
        
        except Exception: 
            return "Conta destino invalida"

    def __str__(self):
        return "conta: {} Titular: {}".format(self.numero, self.titular)
 #heranca
class Poupanca(Conta): 

    def __init__(self, titular, num, saldo):
        super().__init__(titular, num, saldo)
        self.taxa = 0
    
    
    def render_juros(self):
        self.saldo += self.saldo * 0.005
    def sacar(self):  
        return None
