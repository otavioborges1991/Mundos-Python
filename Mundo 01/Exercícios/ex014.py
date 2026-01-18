# converter temperatura de Celsius para Farenheit
import cores
print('Conversor de temperaturas, de ceslsius para farenheit')
celsius = float(input('Digite a temperatura ºC: '))
farenheit = (celsius * 1.8) + 32
print(f'Convertido para farenheit {cores.vermelho}{farenheit:.1f}{cores.nenhum}ºF')