class Cuenta():
    def __init__(self,pro,sal,mon):
        self.__propietario=pro
        self.__saldo=sal
        self.__moneda=mon

    def get_Saldo(self):
        return  self.__saldo
    def get_Propietario(self):
        return  self.__propietario
    def get_Moneda(self):
        return  self.__moneda



    def set_Moneda(self,moneda):
        self.__moneda=moneda

cuenta1=Cuenta("oscar garcia",15000,"soles")
print(cuenta1.get_Saldo())
print(cuenta1.get_Moneda())
cuenta1.set_Moneda("dolares")
print(cuenta1.get_Moneda())

