# Crie uma função voto() que vai receber o prarametro ano de nascimento
# e retorna valor literal se pessoa tem voto: NEGADO, OPCIONAL ou OBRIGATÓRIO.

def voto(nascimento, alfabetizado = True):
    from datetime import date
    idade = date.today().year - nascimento
    print(f'Sua idade {idade}')
    if not alfabetizado or 16 <= idade < 18 or idade > 70:
        return 'FACULTATIVO'
    if idade < 16:
        return 'NEGADO'
    else:
        return 'OBRIGATÓRIO'

resposta = 'Z'
while resposta not in 'SN':
    resposta = str(input('Você é alfabetizado? S/N ').strip().upper()[0])
    if resposta not in 'SN':
        print('Resposta invalida, escreva S para sim ou N para não.')
    if resposta == "S":
        alfabetizado = True
    elif resposta == 'N':
        alfabetizado = False

ano_de_nascimento = int(input('Ano de nascimento: '))
eleitor = voto(ano_de_nascimento, alfabetizado)
print(f"Seu voto é {eleitor}")