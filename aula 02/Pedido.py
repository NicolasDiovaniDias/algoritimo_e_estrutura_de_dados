from Pessoa import Pessoa
from Produto import Produto
import datetime
class Pedido:
    def __ini__(self, cli = Pessoa("Balcão"), data = datetime.date):
        self.id = None
        self.data = data
        self.cliente = cli
        self.Produtos = []

pedido1 = Pedido()
print()