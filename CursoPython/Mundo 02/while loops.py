# while loops
# estrutura de repetição while
# while = enquanto

acumulador = 0
while acumulador != 10: # repetição até que acumulador ser igual a 10, ele pode ultrapassar 10 sem ser 10
    print(acumulador, end=" ")   # fazer o acumulador incrementar 1 não é abrigatório.
    acumulador += 1     # outros processos podem controlar a condição de parada do loop
print('\nAcabou')

while True: # repetição infinita
    print("Oi", end=" ")
    acumulador -= 1
    if acumulador == 0:
        break
print("\nAcabou")

escolha = -1
pares = impares = 0
while escolha != 0: # em quanto a escolha do usuãrio não é 0 o loop continua
    escolha = int(input("Digite um numero: ")) # pede o usuario escolher um numero
    if escolha != 0:                           # continua peding eternamente ate o usuario
        if escolha % 2 == 0:                   # escolher 0
            pares += 1
        else:
            impares += 1
print(f'Foram digitados {pares} numeros pares, e {impares} numeros pares')