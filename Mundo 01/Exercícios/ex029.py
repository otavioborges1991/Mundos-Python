# Leia a velocidade de um carro.
# Se ele passar de 80km/h mostre uma mensagem dizendo que foi multado.
# a multa custa R$7.00 para cada km acima do limite.
import cores

print('Velocímetro')
velocidade = int(input('Digite a velocidade do carro em Km/h: '))
multa = (velocidade - 80) * 7.00
if velocidade > 80:
    print(f'Você foi multado em {cores.verde}R${multa:.2f}{cores.nenhum} reais.')
else:
    print('Bom dia!, dirija com segurança.')