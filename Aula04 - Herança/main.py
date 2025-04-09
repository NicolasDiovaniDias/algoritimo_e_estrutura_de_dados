import sys
from PyQt5.QtWidgets import QApplication

from TelaCategoria import TelaCategoria
from Categoria import Categoria
from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro

app = QApplication( sys.argv )

telaVeiculo = TelaVeiculo( "Cadastro de Veículo")
telaVeiculo.show()

categorias = []
telaCat = TelaCategoria("Adicionar Categoria",categorias)
telaCarro = TelaCarro( "Cadastro de Carro", categorias, telaCat)
telaCarro.show()

sys.exit( app.exec_() )
