# Reescreve a função leia_int() que fizemos no ex104 incluindo a possibilidade de
# digitar números de tipo invalido. Também crie a função leia_float() com a mesma funcionalidade
# ambos com validação de dados.
from utilidadesCeV import dado

inteiro = dado.leia_int('Digite um número inteiro: ')
real = dado.leia_float('Digite um número real: ')

print(f"Numero inteiro {inteiro}, número real {real:.2f}")