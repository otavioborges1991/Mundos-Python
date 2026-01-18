# leia ano de nascimento de 7 pessoas
# mostre quantas maiores de idade e quantas não.
import caixastr
from datetime import date

caixastr.caixa("Contando maiores de idade em uma lista de idades.")
anos = []
maiores = 0
menores = 0
ano = date.today().year
print(ano)
for i in range(0, 7):
    anos.append(int(input("Digite um ano de nascimento: ")))
    idade = ano - anos[i]
    if idade  >= 18:
        print(f'Idade = {idade}, é maior de idade')
        maiores += 1
    else:
        print(f'Idade = {idade}, é menor de idade')
        menores += 1

print(f"A lista contem {maiores} maiores de idade e {menores} menores de idade.")