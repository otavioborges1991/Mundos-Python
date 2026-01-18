# Leia um número real e mostre sua porção inteira.
from math import floor, trunc
import cores
print('Mostrando porção inteira de um número verdadeira (9.5, 13,33333, etc...)')
real = float(input('Digite um numero real: '))
inteiro = int(real) # sem a biblioteca math
# as duas linhas abaixo fazem o mesmo porem usando funções da biblioteca math
piso = floor(real)
truncado = trunc(real)
print(f'''a porção inteira do número real {cores.vermelho}{real}{cores.nenhum} é 
{cores.azul}{inteiro}{cores.nenhum} usando a função int()
{cores.amarelo}{piso}{cores.nenhum} usando a função floor()
{cores.magenta}{truncado}{cores.nenhum} usando a função trunc().''')