# Leia o nome e média de um aluno, e também a situação de um aluno em dicionário
# no final mostre o conteúdo da estrutura na tela.
# média 7 ou mais, aprovado, menos que isso, reprovado.
from cores import verde, vermelho, nenhum

boletim = list()
aluno = dict()
notas = list()
matérias = "Matemática", "Ciência", "Português", "Arte", "Educação Física", "Historia"

while True:
    # Perguntando se quer adicionar mais alunos
    resposta = str(input("Quer adicionar um aluno S/N: ")).strip().upper()[0]
    if resposta not in "SN":
        print("Resposta invalida, digite apenas S para sim ou N para não.")
        continue
    elif resposta in "N":
        break

    # adicionando alunos
    print("Adicionando aluno...")
    nome = " ".join(str(input("Nome: ")).strip().title().split())
    print(f"Adicione as notas do aluno {nome}")
    for matéria in matérias:
        while True:
            nota =float(input(f"Nota de {matéria}: "))
            if nota >10 or nota < 0:
                print('Nota invalida.')
                continue
            else:
                notas.append(nota)
                break
    média = sum(notas) / len(matérias)
    situação = f'{verde}Aprovado{nenhum}' if média >= 7 else f'{vermelho}Reprovado{nenhum}'
    aluno = {'nome': nome, 'média': média, 'notas': notas[:] , 'situação': situação} # notas[:] eu quero uma copia da lista
                                                                                     # a lista tem que zerar depois
    boletim.append(aluno)
    notas.clear() # limpando a lista notas antes de usa-la em para outro aluno
if len(boletim) == 0:
    exit("Nenhum aluno adicionado.")

print(f"{'ID':<4} {'Aluno':^20}{'Média'}")
for n, aluno in enumerate(boletim):
    print(f"{n:<3} {aluno['nome']:_<20}{aluno['média']:>5.1f}  {aluno['situação']}!")

while True:
    print()
    # Perguntando se quer verificar um aluno
    resposta = str(input("Quer verificar um aluno S/N: ")).strip().upper()[0]
    if resposta not in "SN":
        print("Resposta invalida, digite apenas S para sim ou N para não.")
        continue
    elif resposta in "N":
        break
    print()
    resposta = int(input("Verificar aluno pelo ID: "))
    if resposta > len(boletim):
        print('ID não encontrado.')
    else:
        print(f'O aluno de nome {boletim[resposta]['nome']} tirou as seguinte notas')
        for i, matéria in enumerate(matérias):
            print(f'{matéria} = {boletim[resposta]['notas'][i]}')
