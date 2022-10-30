def myfunction(old):
    if old > 18:
        result: str = "Maior de idade"
    elif old == 18:
        result: str = "completou 18 anos"
    else:
        result: str = "Menor de idade"
    return result
    pass


nome = input("What's your name?")
print(nome)

text = 2 + 2
print(text)

age = int(input("Idade"))

resultAge = myfunction(age)

print(resultAge)