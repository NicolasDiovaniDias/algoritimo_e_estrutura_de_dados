class No:
    def __init__(self, valor):
        self.ant = None
        self.dado = valor
        self.prox = None

    def add(self, valor):
        nodo = No( valor )
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        elif nodo.dado < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio.ant = nodo
            self.inicio = nodo
        elif nodo.dado > self.fim.dado:
            nodo.ant = self.fim
            self.fim.prox = nodo
            self.fim = nodo
        else:
            antTestado = self.inicio
            aux = self.inicio.prox
            while aux:
                if nodo.dado < aux.dado:
                    nodo.prox = aux
                    nodo.ant = antTestado
                    antTestado.prox = nodo
                    aux.ant = nodo
                else: 
                    antTestado = aux
                    aux = aux.prox