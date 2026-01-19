import os

def construir_lista():
    pasta_raiz = os.getcwd()
    # print(pasta_raiz)
    perguntas = []
    pasta_perguntas = f'{pasta_raiz}/Mundo 04/desafios/quizz/perguntas' # não esta encontrando o caminho

    for arquivo in sorted(os.listdir(pasta_perguntas)):
        if arquivo.endswith('.txt'):
            caminho = os.path.join(pasta_perguntas, arquivo)
            with open(caminho, 'r', encoding='utf-8') as f:
                linhas = f.readlines()
                pergunta_dict = {}
                for linha in linhas:
                    if ':' in linha:
                        chave, valor = linha.split(':', 1)
                        chave = chave.strip()
                        valor = valor.strip()
                        if chave == 'escolhas':
                            pergunta_dict[chave] = [item.strip() for item in valor.split(',')]
                        else:
                            pergunta_dict[chave] = valor
                perguntas.append(pergunta_dict)

    return perguntas

lista = construir_lista()
print(lista[0]['escolhas'])