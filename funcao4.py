def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True
