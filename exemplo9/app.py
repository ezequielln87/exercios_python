import res # require 'exemplo9.1'

print('Escolha uma opção:')
escolha = ['Big Mac', 'McFlurry', 'McChicken', 'Big Tasty']

object = res.Pedido(escolha)
object.listEscolha(True)

pesquisa = int(input('Qual o número do pedido?'))

resultado = object.getPedido(pesquisa)
print(resultado)

print('---------------------')
print(object.escolha)
print(object.pedidos)
print(object.imprime)
print(object.pedido)
exit()
