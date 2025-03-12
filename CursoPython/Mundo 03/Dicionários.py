# Dicionários são variáveis compotas
dicionario = {} # inicializando um dicionario
dados = dict() # também inicializa um dicionário.

dados = {'nome':'Pedro',  # preenchendo o dicionario com elementos
         'idade':25,      # chave:valor
         'peso': 65.5}    # aqui a chave é peso, o valor é 65.5

print(dados['nome'])  # escrevendo elementos do dicionario chamando suas chavez
print(dados['idade']) # chave idade
print(dados['peso'])  # chave peso

dados['sexo'] = 'M' # criando uma nova chave, sexo, com valor 'M'
print(dados)  # escrevendo o dicionario inteiro
print()
del dados['idade'] # apagando a chave idade e seu valor
print(dados)
filme = {'titulo':'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
print()
print(filme.values()) # escrevendo os valores do dicionario
print(filme.keys())   # escrevendo somente as chavez
print(filme.items())  # escrevendo items, isso é diferente que só escrever o dicionario
print()
for k, v in filme.items():
    print(f'[{k}] = {v}')

# enchendo uma lista com dicionários contendo cada filme
locadora = list()
locadora.append(filme)
filme = {'titulo':'Avengers',
         'ano': 2012,
         'diretor': 'Joss Whadon'}
locadora.append(filme)
filme = {'titulo':'Matrix',
         'ano': 1999,
         'diretor': 'Wachowski'}
locadora.append(filme)
print()
print(locadora[0]['ano'])    # escrevendo o valor da chave ano do filme 0 da lista
print(locadora[2]['titulo']) # escrevendo o valor da chave titulo no filme 2 da lista

print()
pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f"O {pessoa['nome']} tem {pessoa['idade']} anos")
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
del pessoa['sexo']
print()

pessoa['nome'] = 'Leandro'
for k, v in pessoa.items():
    print(f'{k} = {v}')

brasil = [] # lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'} # dois dicionários
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1) # adicionando os dicionários a lista
brasil.append(estado2)
estado = dict()
brasil.clear()
brasil = list()

for c in range(3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla dos Estado: "))
    brasil.append(estado.copy()) # metodo copy() é o jeito certo
                                 # de botar um dicionário numa lista
print(brasil)

# dicionario['chave'] = 'valor' adiciona o valor se não existir, se existir o valor é substituido