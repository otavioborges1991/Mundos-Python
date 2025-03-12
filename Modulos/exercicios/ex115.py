# Crie um sistema modularizado para cadastrar pessoas pelo nome e idade num arquivo de texto simples.
# 3 opções: cadastrar, listar pessoas cadastradas e sair
from utilidadesCeV import dado, interface

opções = "Cadastrar", "Listar", "Sair"
arquivo = "Texto.txt"
interface.cabeçalho('Programa de Registro')

while True:
    interface.cabeçalho('Menu', 20)
    escolha = dado.menu(opções, 20)
    if escolha == "Cadastrar":
        interface.cabeçalho('Cadastrando', 20)
        dado.cadastrar(arquivo)
    elif escolha == "Listar":
        interface.cabeçalho('Listando', 20)
        dado.listar(arquivo)
    elif escolha == "Sair":
        interface.cabeçalho('Saindo', 20)
        break