def site_disponível(url):
    from urllib import request
    try:
        resposta = request.urlopen(url)
        return resposta.getcode() == 200
    except Exception as erro:
        print(f'ERRO: {erro.__cause__}')
        return False
