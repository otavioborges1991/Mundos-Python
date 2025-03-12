# leia o comprimento do cateto adjacente dum triângulo retângulo,
# calcule e mostre o da hipotenusa
# a raíz quadrada dos dois catetos elevados ao quadrado é a hipotenusa.
from math import hypot, sqrt
import cores
print('Calculando Hipotenusa em centímetros')
cateto_oposto = float(input('Comprimento do cateto oposto em cm: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente em cm: '))
# os 3 métodos a baixo calculam hipotenusa.
hipotenusa1 = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1 / 2) # calculando hipotenusa sem a biblioteca math
hipotenusa2 = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2) # sqrt() extrai a raiz quadrada
hipotenusa3 = hypot(cateto_oposto, cateto_adjacente) # hypot() calcula a hipotenusa
print(f'{cores.azul}{hipotenusa1:.2f}{cores.nenhum}')
print(f'A hipotenusa méde {cores.vermelho}{hipotenusa2:.2f}{cores.nenhum} cm')
print(f'{cores.verde}{hipotenusa3:.2f}{cores.nenhum} centímetros')