class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo = 0.0

    def Saldo(self):
        return self.saldo

    def getCliente(self):
        return self.cliente

    def Depositar(self, valor):
        self.saldo += valor

conta1 = Conta('Joao', 1)
conta1.Depositar(float(input('qual o valor do deposito?')))
print(conta1.saldo)
print(conta1.getCliente())

conta2 = Conta('Maria', 2)
conta2.Depositar(200.0)
print(conta2.Saldo())
print(conta2.getCliente())
