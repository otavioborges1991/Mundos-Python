# Leia uma cidade e diga se ela começa com a palavra santo.
import cores
cidade: str = " ".join(input("Digite o nome de uma cidade: ").strip().split())
santo: bool = cidade[:len("santo")].lower() == "santo"

print(f'Cidade {cores.amarelo}{cidade}{cores.nenhum}, começa com santo? {cores.cinza}{santo}{cores.nenhum}')