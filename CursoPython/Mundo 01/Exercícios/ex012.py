# leia um preço e mostre o com 5% de desconto
import cores

print('Analizando desconto:')
preço = float(input('Digite o preço: R$'))
desconto = 5
total = preço - (preço * desconto / 100)
print(f'total a pagar {cores.vermelho}R${total}{cores.nenhum}.')