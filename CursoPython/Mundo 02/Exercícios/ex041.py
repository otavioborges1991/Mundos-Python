# Leia o ano de nascimento e mostre sua categoria.
# Mírin até 9 anos
# infantil até 14 anos
# Júnior até 19 anos
# Senior até 20 anos
# acima é master.
import cores
from datetime import date
print("Classificando para time de natação.")
nascimento = int(input("Em que ano você nasceu: "))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    categoria = "Mirin"
elif idade <= 14:
    categoria = "Intantil"
elif idade <= 19:
    categoria = "Júnior"
elif idade <= 20:
    categoria = "Senior"
else:
    categoria = "Master"
print(f"""O atleta tem {idade} anos de idade
Sua categoria é: {cores.verde}{categoria}{cores.nenhum}.""",)
