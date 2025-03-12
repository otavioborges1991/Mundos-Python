# Operadores aritimeticos.
# Adição (+), subtração (-), multiplicação (*), divisão (/), potência (**)
# Divisão inteira (//) e resto da divisão (%).
num1 = int(input('Digite um numero: '))
num2 = int(input('digite outro: '))
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2 # divisão
pot = num1 ** num2 # potencial mesmo que pow()
intdiv = num1 // num2 # divisão inteira
resto = num1 % num2 # módulo, resto de divisão inteira
print(f'''a soma entre {num1} e num2 é {soma}, subtração é {sub}, divisão {div:.3f}
o produto é {mult} potencia {pot}, divisão inteiro {intdiv} 
e resto desta divisão e´{resto}.''') # .3f em {div:.3f} limita os numeros
# Ordem de precedencia
# 1º: () o que esta dentro de parenteses é feito primeiro. Pode haver
# parenteses dentro deles mesmos, (14 + (4 + 5)), os mais fundo tem precedencia.
# 2º: ** potência depois.
# 3º: (*, /, //, %) se tiver mais de um desses, qual vier primeiro desses é feito
# 4º: (+) e (-) por último.

input('Pressione enter para continuar.')
print(f'5+3*2={5+3*2}') # neste caso 3 × 2 é feito primeiro resultando em 6
# depois soma 5 com o resultado da multiplicação, ou seja, 5 + 6 = 11
print(f'(5+3)*2={(5 + 3) * 2}') # neste a soma 5 + 3 é feito primeiro depois
# o resultado, 8, é multiplicado por 2 resultando em 16.
print(f'3*5+4**2={3*5+4**2}') # 4 ao quadrado resulta em 16, 3 x 5 = 15 então
# 15 + 15 = 31
print(f'3*(5+4)**2={3*(5+4)**2}') # neste caso tem parenteses, então 5+4=9
# então 9 ao quadrado, 81 e finalmente 3x81=243.
print(f'4**3={pow(4,3)}') # usando a função pow() perde a ordem de precedencia.

# usando operadores aritimeticos em string multiplicão as iterações da string
print(f'= * 20 resulta em {'='*20}')
print(f'oi + ola = {"oi" + "ola"}')
