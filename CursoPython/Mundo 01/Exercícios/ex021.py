# abra e reproduza um áudio MP3.
from pygame import mixer, time # contem reprodutor de áudio
import cores
mixer.init()
mixer.music.load('../External/07. Imaginary.mp3')
mixer.music.play()
while mixer.music.get_busy():
    print(f"tocando {cores.azul}Imaginary{cores.nenhum}")
    time.Clock().tick(10)