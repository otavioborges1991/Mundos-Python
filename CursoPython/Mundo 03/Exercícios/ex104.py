# crie função leia_int() que funcione como input() más, só aceite valores
# numéricos.

def leia_int(msg=''):
    leitura = 'a'
    while not leitura.isnumeric():
        leitura = input(msg)
        if not leitura.isnumeric():
            print('ERRO: Digite apenas números inteiros.')
    return leitura

# programa principal
numero = leia_int('Digite números inteiros 0-9: ')
print(f'Seu número digitado foi {numero}')