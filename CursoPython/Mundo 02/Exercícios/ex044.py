# Calcule o valor a pagar, preço normal e condição de pagamento.
# A vista dinheiro ou cheque: 10% de desconto.
# A vista no cartão: 5% de desconto.
# Até 2 vezes no cartão: sem juros.
# 3 vezes ou mais no cartão: 20% de juros.

print("Calculando prestação.")
preço = float(input("Valor da compra: R$"))
formas = ['Dinheiro', 'Cheque', 'Cartão']
pagamento = int(input(f"""Forma de pagamento:
0 - Dinheiro
1 - Cheque
2 - Cartão
Escolha pelo número: """))
if pagamento == 0:
    pagamento = 'Dinheiro'
elif pagamento == 1:
    pagamento = 'Cheque'
elif pagamento == 2:
    pagamento = 'Cartão'
else:
    print('Forma de pagamento invalida')
    exit()

parcelas = int(input("Em quantas vezes?: "))

# este código não cobre todas as formas de pagamento.
if parcelas == 1 and pagamento == 'Dinheiro' or pagamento == 'Cheque':
    total = preço-(preço*(10/100))
    print(f'Total a pagar no {pagamento} com desconto de 10% de desconto R${total}.')
elif parcelas == 1 and pagamento == 'Cartão':
    total = preço-(preço*(5/100))
    print(f'Total a pagar no{pagamento} desconto de 10% R${total}.')
elif parcelas <= 2 and pagamento == 'Cartão':
    total = preço
    print(f'Total a no {pagamento} pagar sem júros R${total}.')
elif parcelas >= 3 and pagamento == 'Cartão':
    total = preço + (preço *(20/100))
    print(f'Total a pagar no {pagamento} com 20% de júros R${total}.')
else:
    exit('Fora do caso (o programa não conta com esta combinação de forma de pagamento + parcelas).')
