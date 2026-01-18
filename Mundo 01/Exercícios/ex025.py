# Leia um nome e diga se ela tem silva no nome
import cores
nome = " ".join(input("Digite um nome completo: ").strip().split()).title()
# tetando encontrar o silva dentro do nome
silva: bool = "Silva" in nome
print(f'teu nome {cores.verde}{nome}{cores.nenhum} tem silva? {cores.amarelo}{silva}{cores.nenhum}')