def leia_dinheiro(msg = str):
    while True:
        valor = str(input(msg))
        valor = valor.replace(',', '.')
        pontos = valor.count('.')

        if pontos > 1:
            print('Dado invalido. use apenas um ponto/virgula')
            continue
        try:
            float(valor)
            break
        except 1:
            print('Dado invalido. use apenas números, e um ponto, ou virgula')

    return valor

def leia_int(msg=''):
    num = int()
    while True:
        try:
            num = int(input(msg))
        except (KeyboardInterrupt, EOFError):
            exit(f'\nUsuário preferiu não informar dados')
        except (TypeError, ValueError):
            print("ERRO: Digite apenas números inteiros.")
        except Exception as erro:
            print(f'ERRO: {erro.__cause__}')
        else:
            break
    return num

def leia_float(msg=''): # modifique para float
    num = float()
    while True:
        try:
            num = float(input(msg))
        except (KeyboardInterrupt, EOFError):
            exit(f'\nUsuário preferiu não informar dados')
        except (TypeError, ValueError):
            print("ERRO: Digite apenas números verdadeiros.")
        except Exception as erro:
            print(f'ERRO: {erro.__cause__}.')
        else:
            break
    return num

def leia_nome(msg):
    while True:
        try:
            nome = " ".join(str(input(msg)).strip().title().split())
        except (EOFError, KeyboardInterrupt):
            exit('\nUsuário decidiu não responder')
        except Exception as erro:
            print(f"Erro {erro.__cause__}")
        else:
            if "0123456789" in nome:
                print("Erro, nome contem digitos:")
            elif """'"!@#$%¨&*()_+=-{[}]?/;:.>,<\\|¹²³£¢¬§ªº°""" in nome:
                print("Erro, nome contem caracteres especiais")
            else:
                return nome

def confirma_nega(prompt='Digite S para sim N para não: ', erro_msg='Escolha Invalida', conf="S", nega='N', skip=False):
    resposta = ""
    while resposta != f'{conf}' and resposta != f'{nega}':
        try:
            resposta = str(input(prompt)).upper()[0]
            if resposta not in f'{conf}{nega}':
                print(f"{erro_msg}")
        except (EOFError, KeyboardInterrupt):
            exit('\nUsuário decidiu não responder')
        except Exception as erro:
            print(f"Erro {erro.__cause__}")
        if resposta == "S":
            return True
        elif resposta == "N":
            return False

def cadastrar(caminho):
    """
    -> Cadastra usuário numa lista dentro dum aquivo de texto simples. Depois pergunta se quer adicionar outro.
        Se a resposta é não o loop termina.
    :param arquivo: Caminho para o arquivo de texto
    :return: Nada
    """

    arquivo = open(caminho, 'a')
    while True:
        nome = leia_nome('Nome: ')
        idade = leia_int('Idade: ')

        arquivo.write(f'Nome: {nome} - Idade: {idade}\n')
        print("Cadastrar outro?")
        continuar = confirma_nega()
        if not continuar:
            break
    arquivo.close()


def listar(caminho):
    arquivo = open(caminho, 'r')
    conteúdo = arquivo.readlines()
    for numero, linha in enumerate(conteúdo):
        print(f'{numero + 1:4>} - {linha}', end="")
    arquivo.close()

def menu(lista, tam = -1):
    """
    -> Mostra um lista com opões e pede para escolher uma.
    :param lista: A lista com as escolhas a serem enumeradas, de 1 até (tamanho da lista)
    :param tam: tamanho da linha usada para alinhamento, por padrão "-1" é igual ao tamanho da lista
    :return: um valor inteiro com o número da escolha.
    """
    if tam == -1:
        tam = len(lista)
    for numero, opção in enumerate(lista):
        print(f'{numero + 1}{opção:_^{tam}}')
    while True:
        resp = leia_int('Escolha: ')
        if resp > len(lista) or resp < 1:
            print('Escolha invalida.')
        else:
            resp = lista[resp - 1]
            return resp