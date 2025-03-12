# Leia um ângulo qualquer. Mostre na tela o valor do seno, cosseno e
# tangente deste ângulo.
import cores

# importando funções para calcular seno cosseno e tangente
from math import tan, cos, sin, radians
print('Descobrindo o seno, cosseno e tangente de um ângulo.')
angulo_graus = float(input('Digite um angulo: º'))
angulo_radiano = radians(angulo_graus)
seno = sin(angulo_radiano)
cosseno = cos(angulo_radiano)
tangente = tan(angulo_radiano)
print(f'''O ângulo de {cores.verde}{angulo_graus}º{cores.nenhum}, ou {cores.azul}{angulo_radiano:.2f}{cores.nenhum} radiano tem
{cores.vermelho}{seno:.2f}{cores.nenhum} de seno
{cores.amarelo}{cosseno:.2f}{cores.nenhum} de cosseno
{cores.fmagenta}{tangente:.2f}{cores.nenhum} de tangente.''')


