# mostre os números pares entre 1 e 50

for numero in range(2, 50 + 1, 2): # numeros que eu quero são apenas pares. então posso começar no 2 e pular de 2 passos
    if numero % 2 == 0:            # de cada vez para poupar trabalho para o maquina.
        print(f'{numero}', end=" ")
