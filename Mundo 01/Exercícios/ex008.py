# leia valor em metros e mostre o em centímetros e milímetros
import cores
print('Convertendo metros para centímetros e milímetros')
metros = float(input('Digite o valor em metros: '))
centímetros = metros * 100
milímetros = centímetros * 10
print(f'{cores.verde}{metros}{cores.nenhum} metros tem {cores.vermelho}{centímetros:.0f}{cores.nenhum} centímetros e {cores.azul}{milímetros:.0f}{cores.nenhum} milímetros.')