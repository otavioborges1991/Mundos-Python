# Estrutura de repetição for.
# Laços de repetição for.
# Laço com variável de controle.

for i in range(1, 10): # iterando entre 1 a 10, parando quando chega no 10
    print(i)           # escreve o número da iteração do range()

itens = ['Jaca', 'Banana', 'Uva', 'Pessego'] # crianda a lista à ser iterada.
for i in itens: # iterando em um lista
    print(i)    # escreve um item da lista por iteração.


vezes = int(input('Quantas vezes você quer spamar ovos?: '))
for i in range(vezes): # iterando ate o número guardado em vezes é alcançado
    print(f"{i} Spam Eggs") # iteraçoes começam com 0. Mesmo que vezes seja 5
                            # e as iteração terminem quando chegem no numero 5
                            # esse laço acontecera 5 vezes por que 0 é um numero.

for i in range(100):
    print(f'{i}', end=" ")
    if i % 2 == 0:
        print('foo', end=" ")
    if i % 3 == 0:
        print('bar', end=" ")
    print()

nome = []
for i in range(4): # iterando para adicionar itens a uma lista
    nome.append(str(input("Digite um nome:")))
print(nome)

# usando for loops diretament em strings
for letra in "Texto":
    print(letra)

# nesse caso a funçao enumerate("Texto") pode retornar o índice de cada
# caractére se for necessário.
for índice, letra in enumerate("Texto"):
    print(f"indice {índice}, letra {letra}")