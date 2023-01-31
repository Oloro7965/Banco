from models.client import Cliente
class conta:
    def __init__(self:object,Cliente:Cliente)->None:
        self.__saldo:float=0
        self.__limite:float=100.0
        self.__numero=Cliente.codigo
        self.__saldoTotal=self.calcular_saldo_total
        self.__cliente:Cliente=Cliente
    def calcular_saldo_total(self):
        return self.__saldo+self.__limite
    @property
    def limite(self):
        return self.__limite
    @property
    def saldoTotal(self):
        return self.__saldoTotal
    @property
    def saldo(self):
        return self.__saldo
    @property
    def Cliente(self):
        return self.__cliente

