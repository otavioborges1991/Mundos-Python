# Condições aninhas são if elif e else dentros uns dos outros.
nomes_casa = ["Otávio", "Larissa", "Jose", "Ana"]
nomes_comuns = ["Pedro", "Maria", "Paulo"]

nome = " ".join(str(input('Qual é o seu nome? ')).strip().title().split())
# este codigo ta falhando em detectar nome de casa quando usa se acento Otavio vs Otávio.
if nome.split()[0] in nomes_casa:
    print('Que nome bonito')
elif nome.split()[0] in nomes_comuns:
    print("Seu nome é comun no brasil")
else:
    print('Tu não é desta casa')
print(f'Tenha um bom dia {nome}')
