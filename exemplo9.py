def listEscolha(escolha):
    for index, item in enumerate(escolha):
        conteudo = [int((index + 1)), str(item)]
        imprime.append(conteudo)
    return imprime

def BuscaSeq(list, item):
    pos =0
    x= False
    while pos<len(list) and not x:
        if list[pos]== item:
            x= True
        else:
            pos = pos +1
    return x

def Pedido(pedido, pesquisa):
   resultado = (BuscaSeq(pedido, pesquisa -1))
   return resultado

print('Escolha uma opção:')
escolha = ['Big Mac', 'McFlurry', 'McChicken', 'Big Tasty']
imprime = []
pedido = []

resultado = listEscolha(escolha)

for index, item in enumerate(escolha):
    pedido.append(index)

print(resultado)
pesquisa = int(input('Qual o número do pedido?'))
# print(pedido)
# exit()


resultado = Pedido(pedido, pesquisa)

if resultado == True:
    print('Pedido solicitado, obrigado pela preferência ;)')

while resultado == False:
    print('Favor escolha uma das opções de pedido válidas')
    pesquisa = int(input('Qual o número do pedido?'))
    resultado = Pedido(pedido, pesquisa)

    if resultado == True:
        print('Pedido solicitado, obrigado pela preferência ;)')