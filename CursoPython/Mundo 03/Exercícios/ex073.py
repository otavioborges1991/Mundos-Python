# Uma tupla com os 20 primeiros do campeonato brasileiro de futebol em ordem de colocação. depois mostre
# Os 5 primeiros
# Os 4 últimos
# A lista em ordem alfabética
# A posição do time chapecoense.
import caixastr, cores

# times em ordem de colocação
times = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia",
         "Cruzeiro", "Vasco", "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude", "Bragantino",
         "Atlético-PR", "Criciúma", "Atlético-GO", "Cuiabá")

caixastr.caixa("Campeonato brasileiro de 2024")
print(f'Times por colocação:')
for lugar, time in enumerate(times):
    print(f'{lugar + 1:2}: {time}')

print(f"\nOs cinco primeiros foram:")
for lugar, time in enumerate(times[:5]): # enumerando os 5 primeiros items
    print(f'{lugar + 1:2}: {time}')

print(f"\nEm ordem alfabética:")
for time in sorted(times): # sorted() ordena os itens em ordem alfabética
    print(f'{time:^20}')

# loop para encontrar em que colocação um time esta.
while True:
    print("Encontre a posição de um time. [Digite fim para terminar o programa]")
    time = str(input("Nome do time:").strip().title())
    if time == "Fim":
        break
    elif time in times:
        print(f"O time {time} esta nesta colocação: {times.index(time) + 1}") # usando metodo index() para achar a
                                                                              # colocação do time no campeonato
    else:
        print(f"{cores.vermelho}Time não esta na lista.{cores.nenhum}")