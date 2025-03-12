# crie uma única tupla com nomes e preços em sequência
# mostre uma listagem de preços organizados em forma tabular e formatada
import caixastr

lista = ("Arroz", 7.50,
         "Leite", 2.5,
         "Pneu", 550.98,
         "Vinho", 70.99,
         "Almofada", 55.50,
         "Notebook", 2345.65,
         "Bolsa", 250.25,
         "Livro", 45.50,)


caixastr.caixa("Lista de compras do super mercado.")
print(f"{'=' * 45}\n{'Listagem de preços':^45}\n{'=' * 45}")
for índice, item in enumerate(lista):
    if índice % 2 == 0:
        print(f"{item:.<30}", end=" | ")
    else:
        print(f"RS {item:>7.2f}")


