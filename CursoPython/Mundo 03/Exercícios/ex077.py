# Uma tupla com várias palavras sem acentos.
# Para cada palavra, mostre suas vogais.

palavras = "Esquimo", "Sobremesa", "Avental", "Southpaw", "Delta", "Alvo", "Pintar", "Cuba", "Desenrolar", "Tres"
vogais = []

for palavra in palavras:
    print(f"A palavra: {palavra:^10} tem as vogais:", end=" ")
    for letra in palavra:              # Loop para encontrar e escrever as vogais
        if letra.lower() in "aeiou":   # Se a letra atual é vogal
            print(letra, end=" ")      # Escreve a letra.
    print() # Após listar as vogais, um print() cria uma nova linha.


