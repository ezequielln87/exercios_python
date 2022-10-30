class Pedido:
    def __init__(self, escolha):
        self.escolha = escolha
        self.imprime = list()
        self.pedidos = list()
        self.numeropedido = int()
    
    def listEscolha(self, init):
        if init == True:
            for index, item in enumerate(self.escolha):
                conteudo = [int((index + 1)), str(item)]
                self.imprime.append(conteudo)
            self.listEscolha(False)
        else:
            for index, item in enumerate(self.escolha):
                self.pedidos.append(index)

    def BuscaSeq(self, item):
        x= False 
        pos =0
        while pos<len(self.pedidos) and not x:
            if self.pedidos[pos]== item:

                x= True
            else:
                pos = pos +1
        return x
    
    def getPedido(self, pesquisa):
        self.numeropedido = pesquisa - 1
        busca = self.BuscaSeq(pesquisa -1)
        if busca == True:
            return True
        else:
            return False


