# primeiros commandos
# var =
# print()
# input()
# assinalar variavel
# string
nome1='Otavio'
idade=34
peso=64.6
# assinar várias variáveis ao mesmo tempo em ordem
x, y, z = 10, 20, 30
# assinar todas as viriaveis o mesmo numero
a = b = c = 100
# imprimindo o console
print('---imprimindo variaveis---')
print(nome1)
print(idade)
print(peso)
print(x, y, z)
print(a, b, c)
nome2: str = 'Vinicios'
nome3: str = 'Borges'
# imprimir sequencia separadas por virgula
# automaticamente coloca espaços
print('---auto colocamento de espaços---')
print(nome1, nome2, nome3)
# imprimir sequencias somadas (com o caractere '+')
# concatena sequencias
print('---Concatenando sequencia---')
print(nome1 + nome2 + nome3)
# usando f'{}' cria
# sequencia formatada
print('---Sequencia formatada---')
print(f'{nome1}{nome2}{nome3}', idade, peso)
# numeros imprimidos com o sinal de + faz com que a soma dos numeros
# seja imprimida, a não ser que sejam escritos como string com os sinais
# ' ou " como dentro de uma função str()
print('imprime a soma das duas variaveis peso e idade')
print(peso + idade)
# usar virgula para imprimir numeros evita que sejam somados
print('imprime as variaves peso e idade na mesma linha')
print(peso, idade)
# comando input() sozinho faz com que python espera
# um dígito antes de continuar o programa, pode ser só apertar enter
input('Pressione enter para continuar')
nome=input('digite seu nome: ')
idade=input('sua idade: ')
peso=input('seu peso: ')
print(f"Seu nome:{nome}, seu peso:{peso} e sua idade:{idade}.")

# comparador em variaveis
a = 15
b = 10
c = a >= b # c = False nesse caso
d = False
e = False
f = d ^ e # retorna True se um desses é True
print(c, f)