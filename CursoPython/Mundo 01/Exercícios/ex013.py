# leia um salário e mostre o com 15 % de aumento.
import cores
print('Calculando aumento de salário.')
salario: float = float(input('Digite seu salário: R$'))
aumento: float = 15.0 # Porcento
novo_salario = salario + (salario * aumento / 100)
print(f'Seu novo salário e de R${cores.vermelho}{novo_salario}{cores.nenhum}.')