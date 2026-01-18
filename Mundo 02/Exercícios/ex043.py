# Leia o peso e a altura, calcule IMC e mostre estado
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida
import cores

print("Calculador de massa corporal. Digite seu peso e altura.")
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura*altura)
print(f"Teu índice de massa corporal é {imc:.2f}.")
if imc < 18.5:
    print(f"Você esta {cores.azul}abaixo do peso ideal{cores.nenhum}.")
elif 18.5 <= imc <= 25:
    print(f'Você esta com {cores.verde}peso ideal{cores.nenhum}.')
elif 25 <= imc <= 30:
    print(f'Você esta com {cores.amarelo}sobre peso{cores.nenhum}.')
elif 30 <= imc <= 40:
    print(f'Você esta com {cores.vermelho}obesidade{cores.nenhum}.')
else:
    print(f'Você esta como {cores.branco}{cores.fvermelho}obesidade mórbida.{cores.nenhum}')