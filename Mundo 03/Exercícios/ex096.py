# faça um programa com uma função chamada area(), que receba as dimensões de um terreno
# largua e cumprimento. e mostre a area de um terreno.

def área(largura, comprimento):
    a = largura * comprimento
    return a


print('Controle de terrenos, declare as dimensões em metros')
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

área = área(largura, comprimento)

print(f'A area é de {área:.2f} metros quadrados')