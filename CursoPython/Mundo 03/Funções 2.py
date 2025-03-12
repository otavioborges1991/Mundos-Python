# interactive help / ajuda interativa.
help(help()) # chama a ajuda interativa
input() # input vazio espera por um enter antes de continuar o programa
help(print()) # na verdade não precisa de um input() para esperar
              # o help().

print(input.__doc__) # também busca por documentação do comando input()


def contador(i, f, p) -> None:
    """
     -> Faz uma contagem e mostra na tela.

    :param i: Início da contagem.
    :param f: Fim da contagem.
    :param p: Passos da contagem.
    :return: None.
    """
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c += p
    print('FIM')

contador(0, 100, 10)
help(contador)


# c = 0 faz esse parametro ser opcional. pode ou não ser informado
# caso não seja, o valor em c = 0 será usado.
def somar(a,b,c = 0):
    s = a + b + c # retornar um resultado não é obrigatório
    return s

print(somar(2, 3, 4))

def teste():
    n = 0 # variaveis declaradas em funções só tem valor dentro da funçao
          # isto é, escopo local
    # gloval n = 0 # global n = 0 usa a variavel global e assinaria ela como 0
    print(f"Na função test o n vale {n}") # se n não for declarada na função, a n global seria usada.

x = 1
n = 2    # ao contrario de variáveis fora de funções, escopo global
teste()

print(f'Na função principal o n vale {n}')
