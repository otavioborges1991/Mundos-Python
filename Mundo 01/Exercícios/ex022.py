# Leia um nome completo e mostre:
#   Com as letras maiúsculas.
#   Com as letras minúsculas.
#   Quantas letras ao todo (sem considerar espaços).
#   Quantas letras tem o primeiro nome.
import cores

Nome: str = " ".join(input("Digite um nome complete: ").strip().split())
NOME = Nome.upper()
nome = Nome.lower()
# descobrir o comprimento do nome sem contar espaços
comprimento = len(nome) - nome.count(" ") # subtraindo a quantidade de espaços do total
# comprimento = len(nome.replace(" ", "")) # ou removendo espaços antes de contar
primeiro = len(nome.split()[0])
print(f"""Teu nome: {cores.verde}{Nome}{cores.nenhum}, eu disse: {cores.fmagenta}{NOME}{cores.nenhum}, isso mesmo {cores.fciano}{nome}{cores.nenhum}.
ele tem {cores.fazul}{comprimento}{cores.nenhum} letras ao todo, e {cores.verde}{primeiro}{cores.nenhum} letras no primeiro nome.
""")