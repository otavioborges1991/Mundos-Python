# tipos primitivos
# int numero inteiro
# função int() pede um numero inteiro, receber um número de ponto flutuante
# ou uma ‘string’ resulta em erro
# números inteiros são numerous sem ponto decimais como 5, −4 0 9495
from unicodedata import numeric

n1 = int(input('digite um numero inteiro: '))
print(n1)
# float pede um número de ponto flutuante ou numero real, com um ponto e
# 4,5 0.056, −15,223, 6,0 são numeros reais, ou de ponto flutuante,
# mas ao contrário da gramática portuguesa, em python o ponto (.) deve
# ser usado para separar as casas decimais.
n2 = float(input('digite um numero real: '))
print(n2)
# boleano ou valor lógico é apenas verdadeiro (True) ou falso (False) esses
# nomes têm que ser capitalizados, primeira letra maiúscula.
# no caso do input() receber qualquer coisa retorna True. ao contrario False
verdade=bool(input('Verdadeiro (True) ou falso (False): '))
print(verdade)
# string() é uma sequencia de caracteres, palavras ou numerous,
# numerous são interpretados como string se tiver aspas entre eles
# aspas vazias ('') é uma string vazia
# 'Olá', '7,5' '12/03/1991' são strings
sequencia=str(input('Digite uma palavra: '))
print(sequencia)
# Digitar valores invalidos para o tipo primitivo sendo pedido resulta em
# erro, string aceita tudo e pode ser formatado se escrito assim
# f'texto {variavel}'.
# o uso de int(), float(), str(), bool() converte o valors de assignações
# como var= ou input() para o seu tipo primitivo.

