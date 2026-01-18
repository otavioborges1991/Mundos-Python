# leia o dia, mês ano de nascimento de uma pessoa e mostre uma mensagem
# com a data formatada
import cores
print('digite sua data de nascimento: ')
dia = int(input('Dia: '))
mes = str(input('Mês: '))
ano = int(input('Ano: '))
print(f'Voce nasceu em {cores.verde}{dia}{cores.nenhum}/{cores.vermelho}{mes}{cores.nenhum}/{cores.azul}{ano}{cores.nenhum}.')
