# Usuário pode digitar vários valores numéricos e cadastre-os numa lista
# Não o adicione se existir.
# Mostre os valores únicos em ordem crescente.
from cores import vermelho, nenhum

lista = []
resposta = "Z"
while True:
    # perguntando se é para continuar
    while resposta not in "SN":
        resposta = str(input("Quer Digitar um número? S/N: ")).upper().strip()[0]
    # avaliando a resposta
    if resposta == "S":
        numero = int(input("Digite um número: "))
    else:
        break
    # checando se número ja esta na lista
    if lista.count(numero) == 0:
        lista.append(numero)
        # Zerando a resposta
        resposta = "Z"
    else:
        print(f"{vermelho}Número duplicado, tente outro.{nenhum}")

#print(sorted(lista)) # função sorted() retorna a lista em ordem crescente, mas não altera a lista
print(f'lista na ordem de entrada {lista}')
lista.sort() # metodo sort() faz a lista ficar em ordem crescente daqui por diante
print(f'lista agora organizada em ordem crescente {lista}')

