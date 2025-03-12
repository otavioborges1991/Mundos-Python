# cria um tupla com 0 a 20 por extenso. ex: um, dois, tres, quatro...
# leia um numero, e mostre ele por extenso usando a tupla
# validação de dados tem que ser feita.
from caixastr import caixa
from cores import verde, vermelho, nenhum, amarelo

numero_extenso = ( "zero", "um", "Dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
           "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

caixa("Escrevendo por extenso.")
while True:
    numero = int(input(f"Digite um numero: {verde}0-20{nenhum}\n"
                       f"{amarelo}[Negativos fecham o programa]{nenhum}\n"
                       f"Número: "))

    # validando o número
    if numero < 0:
        break
    elif numero > 20:
        print(f"{vermelho}Número fora do alcance{nenhum}")
        continue

    # escrevendo por extenso
    print(f"{verde}{numero_extenso[numero]}{nenhum}")

caixa("Fechando")
