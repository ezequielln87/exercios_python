class Pedido:
    def __init__(self, escolha):
        self.escolha = escolha
        self.imprime = list()
        self.pedidos = list()
        self.busca = False
        self.pedido = list()
        self.count = 0
    
    def __str__(self):
        return str(self.imprime)

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
                self.pedido = self.pedidos[pos]
                x= True
            else:
                pos = pos +1
        return x
    
    def getPedido(self, pesquisa):
        while self.count < 3:
            self.count += 1
            self.busca = self.BuscaSeq(pesquisa -1)
            if self.busca == True:
                return str('Pedido solicitado, obrigado pela preferência;)')
            else:
                print(str('Favor escolha uma das opções de pedido válidas \n'+ str(self.imprime) + '\n'))
                pesquisa = int(input('Qual o número do pedido?'))
                self.getPedido(pesquisa)
        return str('Pedido não encontrado, favor tentar novamente mais tarde')

