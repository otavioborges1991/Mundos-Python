# Leia o salário e calcule o aumento. 10% para salários de maiores R$ 1250.00 e 15% de aumento para menores ou iguais.
import cores

salario = float(input('Digite seu salário: R$'))
if salario > 1250.0:
    aumento = 10/100 # 10 porcento
else:
    aumento = 15/100 # 15 porcento
novo_salario = salario + (salario * aumento)
print(f'Seu novo salário com um aumento é {cores.verde}{novo_salario}')
