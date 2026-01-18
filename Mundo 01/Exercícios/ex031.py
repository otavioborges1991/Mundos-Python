# Leia a distância duma viagem em km. Calcule o preço
# da passagem, R$ 0.50 por km em viagens com até 200 km e
# R$ 0,45 em viagens mais longas.
import cores

print('Calculando preço da passagem, baseado em distancia da viagem.')
distância = float(input("Digite a distancia da viagem em Km: "))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print(f'O valor da passagem é {cores.magenta}R$ {preço:.2f}{cores.nenhum} reais.')