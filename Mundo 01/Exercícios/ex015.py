# aluguel de carros, custa R$60.00 por dia, e R$0.15 por km rodado
import cores
print('Calculando valor do aluguel')
dias = int(input('Dias de uso: '))
km = float(input('Quilômetros rodados: '))
total = (dias * 60.00) + (km * 0.15)
print(f'Valor do aluguel: {cores.verde}R${total:.2f}{cores.nenhum}')
