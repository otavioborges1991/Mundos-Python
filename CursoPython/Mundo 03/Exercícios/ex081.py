# Leia vários números e coloque-os numa lista. Depois mostre
# Quantos números digitados.
# A lista em ordem decrescente
# Se o valor 5 esta ou não na lista, e em que posição esta.

lista = []
while True:
    resposta = str(input("Quer digitar um número? S/N: ")).strip().upper()[0]
    # analisando a resposta
    if resposta == "S":
        numero = int(input("Digite um número: "))
        lista.append(numero)
    elif resposta == "N":
        print("Saindo do programa.")
        break
    else:
        print("Resposta invalida. Digite Sim ou Não. ou S ou N")

existe5 = bool(True if lista.count(5) >= 1 else False)
pos5 = "N/A"
if existe5:
    pos5 = lista.index(5)
tamanho = len(lista)
decrescente = sorted(lista, reverse=True)
print(f'''Analisando a lista {lista}.
{tamanho} números digitados.
{f'O número cinco esta na posição {pos5 + 1}' if existe5 else "Não existe 5 na lista"}.
{decrescente} é a lista em ordem decrescente.
''')
