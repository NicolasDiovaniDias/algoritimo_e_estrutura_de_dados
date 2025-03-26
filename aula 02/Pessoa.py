from Cidade import Cidade

class Pessoa:
    def __init__(self, nome, cpf = None, cid = Cidade("Itati")):
        self.id = None
        self.nome = nome
        self.cpf = cpf
        self.cidade = cid
    def __str__(self):
        txt = "Pessoa: "+self.nome
        txt += "\nCPF: "+self.cpf
        txt += "\nCidade: "+str(self.cidade)
        return txt
pessoa1 = Pessoa('nicolas')
pessoa1.__str__()
