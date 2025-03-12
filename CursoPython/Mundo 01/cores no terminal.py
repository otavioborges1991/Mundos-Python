# adicionando cores no stdout
# ansi escape sequence.
# use o codigo "\033[m"
# pacote para colorir texto no terminal
import colors
# \033["codigo do style":"codigo da cor do texto":"codigo do cor do fundo"
# Códigos de estilo.    Cor de texto.       cor de fundo
#   0 sem estilo        30  branco          40 branco
#   1 negrito           31  vermelho        41 vermelho
#   2 "branquito"       32  verde           42 verde
#   3 itálico           33  amarelo         43 amarelo
#   4 sublinhado        34  azul            44 azul
#   5 pisca lento       35  magenta         45 magenta
#   6 pisca rapido      36  ciano           46 ciano
#   7 invertido         37  cinza           47 cinza
#   8 esconder
#   9 cruzado
#   10 fonte padrão
#   11-19 fonte extra
#   20 fraktur

# exmplo \033[1:31:47m
print("\033[0:30:41m exemplo")
print("\033[4:33:44m exemplo")
print("\033[1:35:43m exemplo")
print("\033[30:42m exemplo")
print("\033[m exemplo")
print("\033[7m exemplo\033[m")

print(f"""Testando cores do terminal
Usando dark themes. temas escores, o branco e o preto dever invertidos
\033[0:30:40m testando, um, dois, trez. mais uma vez \033]m
\033[0:30m testando, um, dois, trez. mais uma vez \033]m
\033[1:31:47m testando, um, dois, trez. mais uma vez \033]m
\033[:31:m testando, um, dois, trez. mais uma vez \033]m
\033[2:32:46m testando, um, dois, trez. mais uma vez \033]m
\033[2:33:41m testando, um, dois, trez. mais uma vez \033]m
\033[3:30m testando, um, dois, trez. mais uma vez \033]m
\033[4:35:44m testando, um, dois, trez. mais uma vez \033]m
\033[5:46:43m testando, um, dois, trez. mais uma vez \033]m
\033[5:31m testando, um, dois, trez. mais uma vez \033]m
\033[6:31m testando, um, dois, trez. mais uma vez \033]m
\033[7m testando, um, dois, trez. mais uma vez \033]m
\033[0m testando, um, dois, trez. mais uma vez \033]m
\033[11m testando, um, dois, trez. mais uma vez \033]m
\033[10m testando, um, dois, trez. mais uma vez \033]m
\033[20m testando, um, dois, trez. mais uma vez \033]m
\033[0m testando, um, dois, trez. mais uma vez \033]m
""")


print(f'{colors.cinza}Novo teste usando variaveis importadas')
print(f"{colors.azul}testanto, um, dois, trez.{colors.limpar}")
print(f"{colors.negrito}{colors.verde}testanto, um, dois, trez.{colors.limpar}")
print(f"{colors.italico}{colors.vermelho}testanto, um, dois, trez.")