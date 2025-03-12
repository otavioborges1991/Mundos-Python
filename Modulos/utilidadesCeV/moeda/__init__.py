def aumentar(valor, taxa, formatavel=False):
    if formatavel and type(valor) == float or formatavel and type(valor) == int:
        return True
    if formatavel:
        return valor.isnumeric()
    valor += valor * (taxa / 100)
    return valor

def diminuir(valor, taxa, formatavel=False):
    if formatavel and type(valor) == float or formatavel and type(valor) == int:
        return True
    if formatavel:
        return valor.isnumeric()
    valor -=  valor * (taxa / 100)
    return valor

def dobro(valor, formatavel=False):
    if formatavel and type(valor) == float or formatavel and type(valor) == int:
        return True
    if formatavel:
        return valor.isnumeric()
    valor *= 2
    return valor

def metade(valor, formatavel=False):
    if formatavel and type(valor) == float or formatavel and type(valor) == int:
        return True
    if formatavel:
        return valor.isnumeric()
    valor /= 2
    return valor

def moeda(valor):
    return f"R${valor:.2f}"

def resumo(valor, aumento, diminuição):
    aumentado = aumentar(valor, aumento)
    diminuído = diminuir(valor, diminuição)
    dobrado = dobro(valor)
    metad = metade(valor)
    print(f'''
    Valor Original: {valor}

    {'Ação':<15}{'Total':^10}

    {'aumentado':.<15}{moeda(aumentado)}
    {'diminuído':.<15}{moeda(diminuído)}
    {'dobro':.<15}{moeda(dobrado)}
    {'metade':.<15}{moeda(metad)}
    
    ''')