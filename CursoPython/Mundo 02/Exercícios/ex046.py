# Contagem regressiva de 10 a 0 com intervalo de 1 segundo entre eles
import emoji
from time import sleep


for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print(emoji.emojize('Fogo no Céu todo ano: 🎆'))