# Leia o sexo duma pessoa e só aceite "M" ou "F".

sexo = ""

while sexo not in "MF":
    sexo = str(input("Sexo, masculino ou feminino, escreva M/F: ")).strip().upper()[0] # removendo espaços
                                                                                       # tudo maiúsculo
                                                                                       # e só a primeira letra.
    if sexo not in "MmFf":
        print("Dados inválidos. Por favor informe seu sexo.")
    if sexo in "mM":
        print("Masculino.")
    elif sexo in "Ff":
        print("Feminino.")

print("Confirmado!")
