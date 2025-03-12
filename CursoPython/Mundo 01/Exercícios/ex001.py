# ler o nome duma pessoa e de boas-vindas a ela
import cores

nome=" ".join(input('Digite seu nome: ').strip().title().split())
print(f"Olá {cores.vermelho}{nome}{cores.nenhum}, prazer em te conhecer!")
