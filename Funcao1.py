#Função Cria Matriz Quadrada de espaços (cria mapa)
def cria_mapa(dimensao):
    lista_mapa=[]
    lista_linha=[]
    for i in range (0,dimensao):
           lista_linha.append(' ')
    for i in range (0,dimensao):
        lista_mapa.append(lista_linha)
    return lista_mapa
