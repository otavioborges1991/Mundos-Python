# faça um sistema com o interactive help() do python. usuário digita comando e ajuda aparece.
# no final o usuario pode digitar FIM para o programa encerrar.
# use cores.

resposta = ""
while True:
    print("Ajuda interativa. Digite no nome duma função ou biblioteca, ou sair, para sair.")
    resposta = str(input("Nome: "))
    if resposta == 'sair':
        break
    else:
        help(resposta)




