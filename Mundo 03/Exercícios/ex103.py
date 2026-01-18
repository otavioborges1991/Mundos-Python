# faça função ficha() que receber 2 parâmetros opcionais: nome dum jogador e quantos gols marcou
# o programa tem que mostrar algum dado mesmo que não tenha sido informado corretamente.

def ficha(nome="Desconhecido", gols=0):
    print(f'O jogador: {nome} fez {gols} gols nesta temporada')
    return str(nome), list[gols]

# programa princial
nome = " ".join(str(input('Nome do jogador: ')).strip().title().split())
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == "":
    ficha(gols=gols)
else:
    ficha(nome, gols)
