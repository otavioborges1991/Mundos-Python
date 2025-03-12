def linha(tamanho = 45, char='-'):
    return f'{char * tamanho}'


def cabeçalho(txt="cabeçalho", tam=-1, char='-'):
    if tam == -1:
        tam = len(txt)
    print(f"""
{linha(tam, char)}
{txt.center(tam)}
{linha(tam, char)}""")
