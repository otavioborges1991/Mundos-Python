# tenha uma função chamada contador, com três parametros
# inicio, fim e passo, e realize a contagem
# seu programa tem que realizar 3 contagem atravez desta função
# a) de 1 até 10, de 1 em 1.
# b) de 10 até 0, de 2 em 2.
# c) uma contagem personalizada.

def contador(inicio, fim, passo):
    if inicio > fim and passo > 0:
        exit('ERRO 1: Contador não pode chegar ao fim, inicio maior que fim com passo negativo ou inicio menor que fim com passo negativo')
    elif inicio < fim and passo < 0:
        exit('ERRO 1: Contador não pode chegar ao fim, inicio maior que fim com passo negativo ou inicio menor que fim com passo negativo')
    elif passo == 0:
        exit('ERRO 2: Passos definido como zero')
    for n in range(inicio, fim, passo):
        print(n, end=' ')

    print()

contador(1, 10, 1)
contador(10, 0, -2)
contador(5, 15, 1)
contador(0,0,0)

for n in range(10, 0, 1):
    print(n)
