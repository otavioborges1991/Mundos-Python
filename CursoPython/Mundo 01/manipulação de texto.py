# Manipulação de texto
# string = cadeia, sequencia. de texto "texto" 'texto'
# """texto em varias linhas""" '''texto em varias linhas'''
# usando 3 aspas ou 3 apas duplas permite escrever string em várias linhas.

frase: str = 'Curso em Vídeo Python' # frase de 21 caracteres
# indices começam no 0, então a primeira letra 'C' esta no índice 0
# a última no 20

# fatiando strings com []
print("------Fatiando strings------")
print(frase) # escrevre a frase inteira
print(frase[9]) # [índice] escreve somente o que esta no índice.
print(frase[2:10]) # escreve tudo entre o índice 2 até o 10
print(frase[0:20:3]) # escreve entre os índices 0 e 20 a cada 3 passos
print(frase[15:]) # escreve do índice 15 até o final da string
print(frase[9::2]) # escreve do índice 9 até o final a cada 2 passos
print(frase[:13]) # escreve do começo até o índice 13
print(frase[:4:2]) # do começo até o 4 a cada 2 passos

# analisando a string
print('-----Analisando a string------')
comprimento = len(frase) # len() retorna a comprimento da string
print(f'comprimento da frase {comprimento}')
letrasO = frase.count('o') # frase.count('str') conta as ocorrências de
# uma substring ('str') na frase. Fatiamentos podem ser neste método
# frase.count('o',2,13.2) contando letras 'o' começando no índice 2
# acabando no 13, e a cada 2 passos.
print('contando ocorrencias de uma substring')
print(f'letras "ó" na frase {letrasO}')
deo = frase.find('deo') # frase.find("str")usado para encontrar o índice
# da aonde uma substring ("str") começa.
print('encontrando aonde uma substring começa')
print(f'"deo" começa no caractere número:{deo + 11}')
print(frase.find('Android')) # se a substring não existe, frase.find() retorna -1
print('Curso' in frase) # "'str' em var" retorna True se str é uma substring de var

# transformando strings
print('Transformando strings')
frase.replace('Python', 'Android') # var.replace(str1, str2) retorna
# var com str1 substituida pela str2, mas não muda a string em var
print(frase) # escreve 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android')) # escreve 'Curso em Vídeo Android
print(frase) # escreve 'Curso em Vídeo Python'
# mudança só é permanente se re assinar a variavel
frase = frase.replace('Python', 'Android') # de agora em diante
# print(frase) vai escrever 'Curso em Vídeo Android'
print(frase)
# mudando para letras maiúsculas
print(frase.upper()) # var.upper() retorna a string como letras maiúsculas
# frase = frase.upper() mudaria a fpara todas as letras para maiúsculo permanentemente
frase = frase.lower() # da mesmo forma var.lower() faz tudo em letra minúscula
print(frase)
print(frase.capitalize()) # string.capitalize() faz tudo a primeira palavra
# em maiúsculo, as outras em minúsculos
print(frase.title()) # faz todas as palavras terem primeira letra maiúscula
frase = "   Aprenda Python  "
print(frase.strip()) # .strip() remove espaços em volta da frase
print(frase.lstrip()) # .lstrip() remove somente espaços a esquerda
print(frase.rstrip()) # .rstrip() remove somente espaços a direita
palavras = frase.split() # split(char) divide a string numa lista de palavras
# delimitadas por char, que por padrão é um espaço
print(palavras)
palavras = "-".join(frase.strip()) # "str".join, bota "str" entre cada letra
print(palavras)

# Da de combinar todos estes métodos
frase.upper().find("O") # é um exemplo. para encontrar a letra maiúscula O
# na frase depois de transformar todas as letras em maiúsculas

# rfind() para buscar apartir da direita.

# print condicional
var = 4
print(" x " if var >= 5 else "z") # escreve x se var é maior ou igual a 5, se não, se não escreve y.