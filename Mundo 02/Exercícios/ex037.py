# Leia um número inteiro qualquer e peça ao usuário escolher
# a base de conversão
# 1 binário, 2 octal ou 3 hexadecimal.
import cores

numero = int(input("Digite um numero: "))
escolha = int(input(f"""converter o numero para
[1] binário
[2] hexadecimal
[3] octal
escolha 1-3: """))
# imprimindo em bin() hex() e oct() faz também imprimir o código 0b, 06 e 0o respectivamente
# fatiando strings con string[2:] remove os códigos e só mostra o número convertido
if escolha == 1:
    print(f'O numero {cores.verde}{numero}{cores.nenhum} convertido para binário é {cores.verde}{bin(numero)[2:]}{cores.nenhum}')
elif escolha == 2:
    print(f'O numero {cores.verde}{numero}{cores.nenhum} convertido para hexadecimal é {cores.verde}{hex(numero)[2:]}{cores.nenhum}')
elif escolha == 3:
    print(f'O numero {cores.verde}{numero}{cores.nenhum} convertido para octal é {cores.verde}{oct(numero)[2:]}{cores.nenhum}')
else:
    print("Escolha invalida.")

