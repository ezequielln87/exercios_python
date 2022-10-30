import res
import os

class App:
    def __init__(self ):
        self.opcoes = list()
        self.data = dict()
        self.getData()

    def getResource(self, escolha):
        object = res.Pedido(self.opcoes)
        object.listEscolha(True)
        self.data['imprime'] = object.imprime
        self.data['pedidos'] = object.pedidos
        self.data['numeropedido'] = escolha
        return object.getPedido(escolha)
    
    def getPedidos(self):
        object = res.Pedido(self.opcoes)
        object.listEscolha(True)
        return object.imprime

    def getData(self):
        arq = open("dados.txt") # open file
        linhas = arq.readlines()
        for linha in linhas:
            self.opcoes.append(linha.strip())
        return self.opcoes

os.system('cls')

new_object = App()
print(new_object.getPedidos())
pesquisa = int(input('Qual o número do pedido?   '))
resultado = new_object.getResource(pesquisa)

i=0
while True:
    os.system('cls')
    if i == 2:
            print('Pedido não encontrado, favor tentar novamente mais tarde \n\r')
            break     
    if(resultado == True):
        print('Pedido solicitado, obrigado pela preferência  ;)  \n'+ str(new_object.data['numeropedido']) + '\n\r')
        # print('Pedido solicitado, obrigado pela preferência  ;)  \n\r')
        break
    else:
        i = i+ 1
        print('Favor escolha uma das opções de pedido válidas \n'+ str(new_object.data['imprime']) + '\n\r')
        new_escolha = int(input('Qual o número do pedido? '))
        resultado = new_object.getResource(new_escolha)
        continue
    
# print(new_object.getResource())
# print('--------------------- FINALIZADO ---------------------')
# print(new_object.data['pedidos'])
# print(new_object.data['imprime'])
# print(new_object.data['numeropedido'])
# exit()
