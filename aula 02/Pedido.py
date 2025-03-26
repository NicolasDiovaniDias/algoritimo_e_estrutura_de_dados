from Pessoa import Pessoa
from Produto import Produto
import datetime
class Pedido:
    def __ini__(self, cli = Pessoa("Balcão"), data = datetime.date):
        self.id = None
        self.data = data
        self.cliente = cli
        self.Produtos = []

    def addProd(self, prod):
        if prod != None and prod.preco>=10:
            self.Produtos.append(prod)
        soma = 0.0
        for p in self.Produtos:
            soma+= p.preco
        return soma
    def __str__(self):
        txt = "Pedido realizado em: " + str(self.data)
        # txt += "\nCliente: " + self.cliente.nome
        txt += "\nCliente: " + str(self.cliente)