class Carro:
    def __init__(self, modelo, ano = 2006):
        self.modelo = modelo
        self.ano = ano
        self.__kilometragem = 0
    def SetKM(self, km):
        if km  > self.__kilometragem:
            self.__kilometragem = km
    def incrementar(self, km):
        if km > 0:
            self.__kilometragem = km
    def __str__(self):
        txt = "modelo: "+self.modelo
        txt +="\nAno: "+str(self.ano)
        txt +="\nKilometragem: "+str(self.__kilometragem)
        return txt
x = Carro("nicolas", 2004)
print(x)