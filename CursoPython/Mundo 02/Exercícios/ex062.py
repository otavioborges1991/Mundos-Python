# Melhores o ex061, pergunte se o usuário quer mostrar mais termos.
# Mostre até que ele queira 0 termos.
import caixastr

print("Gerando progressão aritmética.")
inicio = int(input("Inicio: "))
razão = int(input('Razão: '))
termos =int(input('Termos: '))

caixastr.caixa("Progressão aritmética.")
i = inicio
while i < (termos * razão):
    print(f'{i} ->', end=" ")
    i += razão
    if i >= (termos * razão):
        print("Acabou!")
        termos += int(input("Mostrar mais termos? (0 para finalizar): "))
