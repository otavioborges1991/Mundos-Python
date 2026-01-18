# leia o nome e duas notas de vários alunos, e guarde tudo em uma lista composta.
# Mostre um boletim contendo a média de cada aluno e permita o usuário mostrar
# a nota de cada aluno que ele escolher separadamente.
# uma lista com cada aluno, cada aluno tem uma lista com notas dentro


ficha = list()

resposta = "S"
print("Adicionando Alunos")
while resposta not in "N":
    # validando resposta
    resposta = str(input("Quer adicionar aluno: S/N: ")).strip().upper()[0]
    if resposta not in "SN":
        print("Resposta invalida")
        continue
    elif resposta in "N":
        break

    # pegando dados dos alunos,
    nome = " ".join(str(input("Nome: ")).strip().title().split())
    print(nome)
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = float((nota1 + nota2) / 2)
    ficha.append([nome, [nota1, nota2], media])

if len(ficha) == 0:
    exit("Nenhum aluno registrado")

print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
for indice, aluno in enumerate(ficha):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")


# novo loop para visualizar dados dos alunos.
while True:
    resposta = str(input("Quer ver notas de um aluno: S/N: ")).strip().upper()[0]
    if resposta not in "SN":
        print("Resposta invalida")
        continue
    elif resposta in "N":
        break

    indice = int(input("Digite o número do aluno: "))

    if indice >= len(ficha):
        print("Aluno não encontrado")
        continue
    else:
        print(f"Notas de {ficha[indice][0]} são {ficha[indice][1]}")
