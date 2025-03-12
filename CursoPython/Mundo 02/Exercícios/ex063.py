# Leia um número "N" inteiro e mostre os "N" primeiros números duma sequência fibonacci.
# 0 1 1 2 3 5 8
import caixastr

caixastr.caixa("Mostrando sequencia de fibonacci")
termos = int(input("Quantos termos mostrar: "))
iteração = 0

# sequencia de fibonacci em while loop
print("Fibonacci em while loop")
while iteração < termos:
    if iteração == 0:
        acumulador1 = 0
        print(acumulador1, end=" ")
    elif iteração == 1:
        acumulador2 = 1
        print(acumulador2, end=" ")
    else:
        acumulador3 = acumulador1 + acumulador2
        print(acumulador3, end=" ")
        acumulador1 = acumulador2
        acumulador2 = acumulador3

    iteração += 1
print('\n',"FIM")
print("fibonacci em for loop")
for i in range(termos):
    if i < 2:
        acumuladorA = 0
        acumuladorB = 1
        print(i, end=" ")
    else:
        acumuladorC = acumuladorA + acumuladorB
        print(acumuladorC, end=" ")
        acumuladorA = acumuladorB
        acumuladorB = acumuladorC

print('\n', "FIM")