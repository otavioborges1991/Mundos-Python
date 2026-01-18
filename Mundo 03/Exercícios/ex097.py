# faça um programa com a função escreva() que receba um texto qualquer
# como parâmetro e mostre uma menssagem com tamanho adaptavel.
# cercados por linhas em cima e em baixo

def escreve(msg, linha = '*'):
    print(f"{linha * (len(msg) + 4)}")
    print(f"{linha} {msg} {linha}")
    print(f"{linha * (len(msg) + 4)}")

escreve('Ola mundo!')
escreve('Curso em Vídeo Python')
escreve('CeV')
escreve('Um dois tr')
