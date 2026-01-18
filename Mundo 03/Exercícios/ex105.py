# faça função notas() que receba variás notas de alunos e vai retornar um dicionario com
# quantidade de notas. A maior nota. A menor nota. A média da turma. A situação (opcional)
# situações, boa, ruim, razoável.
# adicione docstings da função.

def notas(* notas, sit):
    '''
    -> calcula a situação duma turma de escola com base na média de notas.
        Retorna total de notas, maior e menor notas, média de notas e (opcional) situação.
    :param notas: Lista de notas dos alunos
    :param sit: Situação da média da turma, boa, ruim, razoável.
    :return:
    '''
    maior = max(notas)
    menor = min(notas)
    total_de_notas = len(notas)
    media = sum(notas) / len(notas)
    lista = {'total de notas': total_de_notas ,'maior nota': maior ,'menor nota': menor ,'media': f'{media:.1f}'}
    if sit:
        if media < 6:
            situação = "RUIM"
        elif 8 > media >= 6:
            situação = "RAZOAVEL"
        else:
            situação = "BOA"
        lista['situação'] = situação

    return lista

# programa principal
resposta = notas( 5.5, 7.5, 10, sit=True)
print(resposta)

# help(notas) # mostra a docstring da minha função