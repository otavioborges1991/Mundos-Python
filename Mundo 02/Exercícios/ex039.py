# Leia o ano de nascimento dum jovem e informe, conforme a idade dele
# Se ele terá que se alistar ao serviço militar.
# Se é hora de se alistar.
# Se já passou da hora de se alistar.
# Mostre quanto tempo falta ou passou do prazo de se alistar.
from datetime import date
import cores

nascimento = int(input("Em que ano você nasceu: "))
ano = date.today().year
idade = ano - nascimento
alistamento = abs(idade - 18) # calcula a diferença entre idade atual e idade de alistamento para saber quantos anos
                              # falta ou se passaram.
                              # abs() valor absoluto, converte negativo "-5" em positivo "5"

if idade < 18:
    print(f"voce ainda tem que se alistar em {cores.verde}{alistamento}{cores.nenhum} anos")
elif idade == 18:
    print("Ta na hora de se alistar.")
else:
    print(f"Já passou da hora de se alistar em {cores.vermelho}{alistamento}{cores.nenhum} anos")
