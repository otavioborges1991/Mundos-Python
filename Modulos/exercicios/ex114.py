# crie um código em python que teste se o site pudim.com.bt está acessível pelo computador usado.
from utilidadesCeV import web, cores

url = 'https://www.pudim.com.br/'
online = web.site_disponível(url)
if online:
    print(f"O site {cores.magenta}{url}{cores.nenhum} está {cores.verde}online{cores.nenhum}.")
else:
    print(f"O site {cores.magenta}{url}{cores.nenhum} está {cores.vermelho}online{cores.nenhum}.")

