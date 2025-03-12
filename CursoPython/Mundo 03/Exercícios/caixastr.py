def caixa(msg: str, linha: str="*"):
    print(f"{linha * (len(msg) + 4) }")
    print(f"{linha} {msg} {linha}")
    print(f"{linha * (len(msg) + 4)}")
