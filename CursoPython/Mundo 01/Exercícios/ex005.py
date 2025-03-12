# leia um número e mostre seu sucessor e seu antecessor
import cores

num = int(input('Digite um número: '))
ant = num-1
suc = num+1
print(f'antes de {cores.vermelho}{num}{cores.nenhum} vem {cores.azul}{ant}{cores.nenhum} e depois vem {cores.amarelo}{suc}{cores.nenhum}.')