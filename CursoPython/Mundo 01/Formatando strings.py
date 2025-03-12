# formatando strings
nome = input('Teu nome? ')
print(f"olá {nome:20}!") # :20 faz com que o texto inteiro da variavel nome seja
# formatada em 20 espaços, adicionando espaços caso o nome tenha menos
# de 20 caracteres.
print(f"olá {nome:<20}!") # < alinha a esquerda, como de padrão
print(f"olá {nome:>20}!") # > alinha a direita.
print(f"olá {nome:^20}!") # ^ centraliza

print(f"olá {nome:=^20}!") # =, que pode ser substituido
# por qualquer dígito, preenche os espaços restantes.
# tando o = quando ^ e o 20 podem ser substituidos por variaveis
digito = input('digite algo qualquer: ')
alinhamento = input('< ^ > ?')
espacos = input('espaços: ')
print(f"olá {nome:{digito}{alinhamento}{espacos}}!")
input('aperta enter pra continuar')
num1 = float(input('digite um numero real:'))
num2 = float(input('digite outro: '))
div = num1 / num2
print(f"{div:.3f}") # .3f aqui limita a mostra apenas 3 casas decimais
decimos = int(input('digite numero inteiro:'))
print(f"{div:.{decimos}f}") # os números de casas decimais podem variar
print("Isso é tudo", end=' ') # , end=' ' faz com que o print() não termine em
# uma nova linha
print(f'pessoal.\nou não é?') # \n faz com que o texto continue em nova linha
