# Leia uma frase e diga.
#   Quantas letras a.
#   Qual posição que ela apareceu primeiro.
#   Qual a posição que apareceu por último.
import cores

frase: str = " ".join(input("Digite uma frase: ").strip().split()).capitalize()
letrasA: int = frase.lower().count('a')
primeiroA: int = frase.lower().find('a')
ultimoA: int = frase.lower().rfind('a')

print(f'''A frase:
{cores.fvermelho}{frase}{cores.nenhum}
tem {cores.vermelho}{letrasA}{cores.nenhum} letras A
a primeira aparece na posição {cores.verde}{primeiroA + 1}{cores.nenhum}
a ultima no posição {cores.fverde}{ultimoA + 1}{cores.nenhum}''')