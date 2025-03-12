# def nome_da_função()
# def para inicializar a definição de uma função.
# lin é o nome desta função,
def lin(comprimento): # comprimento e um parametro
    print("-" * comprimento)      # passado para esta linha

def titulo(txt):
    lin(30)                   # usando uma função dentro da outra
    print(txt)
    lin(30)

def contador(* num):
    tam = len(num)  # * num neste caso desempacota um número indeterminado
    resultado = 0   # de elementos para ser usados na função
    for n in range(tam):
        resultado += num[n]
    return resultado

def dobra(lista):      # se o argumento for uma lista não é preciso desempacotar.
    for item in range(len(lista)):
        lista[item] *= 2


titulo("Curso em vídeo")

def soma(a = type[int], b = type[int]) -> int: # essa função faz o mesmo que sum()
    return a + b

print(soma(14, 54))
print(soma(a=15, b=10)) # se fazer explicito a=15, b=10, deve estar em order
# soma(b=15, 15) não posso botar o a depois de deixar explicito o b, mas deixar explicito o a funciona
print(contador(1, 3, 4, 5, 6))
valores = [1, 3, 4, 5, 6]
dobra(valores)
print(valores)
