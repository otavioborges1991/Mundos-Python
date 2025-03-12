# Leia uma frase e diga se é um palíndromo.
# Desconsiderando espaços.
import caixastr, cores

caixastr.caixa("Identificando Palíndromos, podem ser lidos de trâs para frente, e continuar sendo a mesma coisa.")
# Identificar palíndromos, requer remover espaços, pontuação e acentos. Este código só remove espaços.
frase = "".join(str(input("Digite uma frase qualquer:")).strip().split()).lower() # remove espaços
inverso = frase[::-1].lower() # frase de trás para frente e em minúsculos

print(f'O inverso de {frase} é {inverso}')
if inverso == frase:
    print(f'{cores.fverde}{cores.branco}É palíndromo.{cores.nenhum}')
else:
    print(f'{cores.fvermelho}{cores.branco}Não é palíndromo.{cores.nenhum}')
