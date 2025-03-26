class Produto:
    def __init__(self,nome,preco=10.0,qtn=0):
        self.id=None
        self.nome=nome
        self.preco=preco
        self.qtn=qtn
    def __str__(self):
        txt = "Produto: "+self.nome
        txt += "\nPreço: "+str(self.preco)
        return txt