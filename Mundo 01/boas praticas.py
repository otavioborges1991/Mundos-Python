# Boas práticas

# Anotações de tipo.
# : "tipo" = ajuda o ide a identificar o tipo da variável, pode mostrar possíveis erros.
from typing import Final # importar somente as funções necessárias.

numero_inteiro: int = 6
numero_real: float = 17.0
frase: str = 'Olá Múndo!'
verdade: bool = True
# "Final" declara uma variável como imutável. Não faz a variável imutável em tempo de execução, mas ajuda IDE a
# identificar erros.
PI: Final[float] = 3.14159265358979323846

print(PI)


# Ao receber nome de alguem com input() usar
# " ".join(input("").strip().split()).title()
# como no exemplo a baixo, remove espaços desnecessários.
# Mesmo que o usuário escreva algo como:"  Oslavo   de     Carvalho  ".
# O nome na variável será: "Oslavo de Carvalho".
# title() faz a primeira letra de cada nome ser maiuscula e as outras minusculas.
# sem title() caso não seja o nome completo de alguem.
# capitalize() se for uma frase.
nome: str = " ".join(input("Digite um nome completo: ").strip().split()).title()
print(f'{nome.title()}.')