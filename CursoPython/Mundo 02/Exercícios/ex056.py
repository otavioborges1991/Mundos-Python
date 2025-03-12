# Leia nome idade e sexo de 4 pessoas. Mostre
# Média de idade do grupo
# Nome do Homem mais velho
# Quantas mulheres tem menos de 20 anos.
import caixastr
nomes = []
idades = []
sexos = []
média = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_jovens = 0

caixastr.caixa('Calculando Nomes idades e sexo')
for i in range(0,4):
    print(f'{'='*5} Pessoa {i+1} {5*'='}')
    nomes.append(" ".join(str(input('Digite um nome: ')).strip().title().split()))
    idades.append(int(input('Digite uma idade: ')))
    sexos.append(str(input('Sexo [1] Masculino [2] Feminino: 1/2 M/F:')).strip())
    if sexos[i][0] in '1Mm':
        sexos[i] = 'Masculino'
    elif sexos[i][0] in '2Ff':
        sexos[i] = 'Feminino'
    if sexos[i] == 'Masculino' and idades[i] > idade_homem_mais_velho:
        idade_homem_mais_velho = idades[i]
        nome_homem_mais_velho = nomes[i]
        print(f"Ate agora {nomes[i]} é o homem mais velho")
    if idades[i] < 18 and sexos[i] == 'Feminino':
        mulheres_jovens += 1
        print(f'Ate agora em {mulheres_jovens} mulheres com menos de 18')

caixastr.caixa('Lista completa')
for i in range(0, len(nomes)):
    print(f"{nomes[i]}, {idades[i]} {sexos[i]}""")

caixastr.caixa("Resultado")
média = sum(idades) / len(idades)
print(f"""O homem mais velhor é {nome_homem_mais_velho}, ele tem {idade_homem_mais_velho} anos de idade.
A lista contém {mulheres_jovens} mulheres menores de 18 anos.
A média das idades é {média}.""")

