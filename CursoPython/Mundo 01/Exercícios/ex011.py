# leia largura e altura duma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, cada litro pinta 2m²
import cores

print('Calculando volume de tinta necessária para pintar.\nDigite as dimensões das paredes a serem pintadas.')
altura = float(input('Altura: '))
largura = float(input('Largura: '))
area = float(altura * largura)
litros = area / 2
print(f'''Sua parede tem {cores.azul}{altura:.2f}{cores.nenhum}x{cores.vermelho}{largura:.2f}{cores.nenhum}, totalizando {cores.verde}{area:.2f}{cores.nenhum} metros quadrados.
{cores.amarelo}{litros}{cores.nenhum} litros de tinta serão o bastante''')