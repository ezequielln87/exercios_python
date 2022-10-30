def BuscaBin(list, item):
    prim = 0
    ult = len(list) -1
    found = False


    while prim <= ult and not found:
        meio = (prim + ult) // 2

        if list[meio] == item:
            found = True
        else:
            if item < list[meio]:
                ult = meio - 1
            else:
                prim = meio + 1

    return found



lista = [42, 32, 19, 17, 13, 8, 2, 1, 0, ]
lista.sort()
# print(lista)
# exit()
buscar = int(input("Digite um número para buscar na lista?"))

resultado = BuscaBin(lista, buscar)

if resultado == True:
    print(f'O valor {buscar} encontra-se na lista')
else:
    print(f'O valor {buscar} não foi encontrado na lista')

# print(BuscaBin(lista, buscar))