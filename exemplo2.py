def CalculoSalario():
    imposto = 27.
    while imposto > 0.:
        imposto = input("Imposto ou (s) sair:")
        if not imposto:
            imposto = 27.
        elif imposto == 's':
            break
        else:
            imposto = float(imposto)
        print("Valor FInal:{0}".format(salario - (salario * imposto * 0.01)))


salario = int(input("Valor Salario:"))
CalculoSalario()