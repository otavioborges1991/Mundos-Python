# Leia 5 valores numéricos e cadastre-os numa lista já na ordem crescente
# sem precisar usar sort(). Mostre a lista na tela.

lista = []
for iteração in range(5):
    número = int(input("Digite um número: "))
    # checando aonde inserir o número
    if iteração == 0 or número > lista[-1]: # checando se é o primeiro número ou se é maior que o ultimo
        lista.append(número)                # se for é inserido imediatamente

    else:                    # checando em que posição da lista deve ser inserido.
        posição = 0
        for posição in range(len(lista)):
            if número < lista[posição]:        # comparando se o número é menor que o na posição.
                lista.insert(posição, número)  # se for, inserira-o nesta posição
                break                          # e então sai do loop


print(f'A lista completa tem os seguintes números {lista} em ordem crescente')
