aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))

if aluno['media'] >= 7:
    aluno['situaçao'] = "aprovado"

else:
    aluno['situaçao'] = "Reprovado"

for x, y in aluno.items():
    print(f'-{x} é igual a {y}')

print(aluno.keys())
print(aluno.values())