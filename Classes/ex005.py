'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes
atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e
saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
>>> yhago = contaCorrente(493979, 'Yhago Carvalho')
>>> yhago.deposito(500)
>>> yhago.mostraSaldo()
500
>>> yhago.deposito(1000)
>>> yhago.mostraSaldo()
1500

'''

class contaCorrente():
    def __init__(self, num_conta, nome, saldo = 0):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, saldo):
        self.saldo += saldo

    def saque(self, saldo):
        self.saldo -= saldo

    def mostraSaldo(self):
        return self.saldo
