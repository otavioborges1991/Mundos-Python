# crie um programa que tenha uma função fatorial() que recebe dois parametros
# um indica número a calcular, o outro chamado show, que será um valor lógico opcional
# indicando se será mostrado ou não na tela o processo de cálculo

def fatorial(num, show=False):
    """
    -> calcula o fatorial de um número e opcionalmente, mostre o calculo
    :param num: Número a ser calculado o fatorial
    :param show: True para mostrar o calculo sendo feito
    :return: Fatorial de num
    """
    total = 0
    if show: print(f'{num}!=', end="")
    for n in range(num, 0, -1):
        if n == num:
            total = n
        else:
            total *= n
        if n > 1:
            if show: print(f'{n}x', end="")
        elif n == 1 or n == 0:
            if show: print('1=', end="")
    return total


print("Calculo fatorial")
numero = int(input("Digite um numero: "))
print(f'O resultado do calculo fatorial de {numero}')
print(fatorial(numero, show=False))