# leia quanto dinheiro tem na carteira e mostre quantos dólares pode comprar
import cores


real = float(input('Quantos Reais você tem? R$'))
cotação = 6.07
dollars = real / cotação
print(f'Você pode compara {cores.verde}${dollars:.2f}{cores.nenhum} Dollars com seus {cores.vermelho}R${real:.2f}{cores.nenhum} Reais.')
