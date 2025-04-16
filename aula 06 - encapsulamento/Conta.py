class Conta:
    def __init__(self):
        self.__saldo = 0.0
    def getSaldoI(self):
        return self.__saldo
    def setSaldo(self, valor):
        self.__saldo = valor