# Leia pelo teclado e mostre o seu tipo primitivo e todas as informações
# possiveis sobre ele.
import cores

var=input('Digite algo: ')
print(f"""
o tipo primitivo é {cores.azul}{type(var)}{cores.nenhum}
é alfa numerico? {cores.vermelho}{var.isalnum()}{cores.nenhum}
é alfabetico? {cores.verde}{var.isalpha()}{cores.nenhum}
é ascii? {cores.amarelo}{var.isascii()}{cores.nenhum}
é Digito? {cores.ciano}{var.isdigit()}{cores.nenhum}
é tudo minusculo? {cores.magenta}{var.islower()}{cores.nenhum}
é decimal? {cores.cinza}{var.isdecimal()}{cores.nenhum}
é identificador? {cores.negrito}{var.isidentifier()}{cores.nenhum}
é numero? {cores.italico}{var.isnumeric()}{cores.nenhum}
é printavel? {cores.fciano}{var.isprintable()}{cores.nenhum}
é tudo espaço? {cores.fazul}{var.isspace()}{cores.nenhum}
é capitalizado? {cores.fverde}{var.istitle()}{cores.nenhum}
é tudo maiúsculo? {cores.fmagenta}{var.isupper()}{cores.nenhum}
""")