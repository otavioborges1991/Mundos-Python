# importando biblioteca
import random # imorta a biblioteca random
from math import ceil, floor, trunc # da biblioteca math, import as função ceil(), floor() and trunc()
import emoji # bibliotecas externas tem que instalar antes de usar

num1 = random.randint(1, 10) # usando a função randint() da biblioteca random
num2 = random.random()
print(f'numeros gerados com a biblioteca random, randint {num1}, random {num2}')
ceil = ceil(num2)
print(f'numero gerado com randint e depois passado pela função ceil {ceil}')
floor = floor(num2)
print(f'mesmo numero mas desta vez pela função floor {floor}')
trunc = trunc(num2)
print(f'e finalmente pela função trunc {trunc}')
print(f'Novo emoji instalado com o biblioteca emuji {emoji.emojize('😂')}')
