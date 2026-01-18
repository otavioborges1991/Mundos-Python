# Leia nome, ano de nascimento e carteira de trabalho e cadastra com idade num dicionário
# se a CTPS for diferente de zero, o dicionário também recebe o ano de contratação e o salário.
# calcule a crescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Aposentadoria é 35 anos de contribuir, CTPS carteira de trabalho da previdencia social.
from datetime import date


print("Cadastrando documento")
nome = " ".join(str(input("Nome: ")).strip().title().split())
ano_de_nascimento = int(input("Ano de nascimento: "))
idade = date.today().year - ano_de_nascimento

CTPS = True if str(input("Tem carteira de trabalho: ").strip().upper()).strip()[0] in "S" else False
if CTPS:
    carteira_de_trabalho = int(input("Numero da carteira de trabalho: "))
    ano_de_contratação = int(input("Em que ano começou a trabalhar: "))
    salário = float(input("Seu salário R$"))
    ano_de_aposentadoria = ano_de_contratação + 35
    idade_de_aposentadoria = ano_de_aposentadoria - ano_de_nascimento
else:
    carteira_de_trabalho = ano_de_contratação = salário = ano_de_aposentadoria = idade_de_aposentadoria = False

pessoa = {'nome': nome, 'ano de nascimento': ano_de_nascimento, 'carteira de trabalho': carteira_de_trabalho,
          'idade': idade, 'ano de contratação': ano_de_contratação, 'salário': salário,
          'aposentadoria': ano_de_aposentadoria, 'idade da aposentadoria': idade_de_aposentadoria}

for chave, valor in pessoa.items():
    if valor:
        print(f'{chave:.<30}:{valor}')