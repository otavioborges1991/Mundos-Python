#

try: # tente executar o bloco abaixo
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))
    resultado = numerador / denominador
except Exception as erro: # se não funcionar, então except vai executar
                          # Exception contem as informações que são armazenadas na variavel erro.
                          # erro.__algo__ pode ser usado para reduzir os detelhes mostrados sobre o problema na variavel
    print(f"Algum problema: {erro.__class__}") # por exemplo erro.__class__ mostra a classe do erro.
else: # se o try funcionar o else também vai
    print(f'Resultado = {resultado:.1f}')
finally: # finally vai executar quere try funcione ou não.
    print('Volte sempre')


# de novo
try:
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))
    resultado = numerador / denominador
except TypeError: # TypeError é qual essa exceção tratara. no casso erro de tipo. Exception como na tentaiva acima é
                  # generico e trata de todos os erros que não saem do programa. TypeError e outros são especificos
                  # Multiplos except podem ser colocados
    print(f"Erro de tipo")
except ValueError:
    print(f"Erro de valor")
except OSError:
    print(f"Erro de sistema operacional")
else:
    print(f'Resultado = {resultado:.1f}')
finally:
    print('Volte sempre')


try:
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))
    resultado = numerador / denominador
except (TypeError, ValueError): # mais de um tipo de erro pode ser tratado no mesmo except
                                # neste casso erro de tipo e de valor
    print(f"Tipos de dados inválidos")
except ZeroDivisionError:
    print(f"Não é possivel dividir por zero")
except KeyboardInterrupt:
    print(f'Usuário preferiu não informar dados')
except EOFError:
    print("Fim da linha meu amigo")
except Exception as erro: # depois de tantos erros especificados, um erro generico como Exception pode pegar o resto
                          # dos erros esquecidos pelas exceções acima
    print(f"Um erro generico foi {erro.__cause__}") # erro.__cause__ vai mostrar a causa do erro.
else:
    print(f'Resultado = {resultado:.1f}')
finally:
    print('Volte sempre')