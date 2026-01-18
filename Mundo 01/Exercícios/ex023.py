# Leia um número de 0 a 9999 e mostre cada dígito.
#   Unidade
#   Dezena
#   Centena
#   Milhar
import cores

numero = int(input("Digite um numero entre 0 e 9999: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'''{cores.fazul}{numero}{cores.nenhum}
unidade {cores.famarelo}{unidade}{cores.nenhum}
dezena {cores.fverde}{dezena}{cores.nenhum}
centena {cores.fciano}{centena}{cores.nenhum}
milhar {cores.fmagenta}{milhar}{cores.nenhum}''''')