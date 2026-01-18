# Condições.
# if var1 == va22:
#   then...
# elif var1 == var3:
#   then...
# else:
#   then...

nota1: float = float(input("Digite uma nota: "))
nota2: float = float(input("Digite outra nota: "))
média: float = (nota1 + nota2) / 2
print(f"A sua média foi: {média:.1f}")
if média >= 6: # se a média é maior ou igual a 6...
    print('Parabéns') # escreva "Parabéns",
else: # se não...
    print('Estude mais!') # escreva "Estude mais".
print('Parabéns' if média >= 6 else 'Estude mais!') # o mesmo de antes mas agora tudo dentro de um print().
print('Parabéns') if média >= 6 else print('Estude mais!') # mais uma vez, a mesma coisa em uma linha e 2 print().
