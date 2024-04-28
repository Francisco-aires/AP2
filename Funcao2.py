# Função posição suporta (ainda precisa ser corrigida e enviada na academia python)
def posicao_suporta(mapa,n_blocos,linha,coluna,orientacao):
    if orientacao=='h':
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if (coluna+i)>len(mapa[linha])-1:
                return False #peça fora do mapa
        for i in range(0,n_blocos):#posição ocupada pelo bloco
            if mapa[linha][coluna+i]=='N':
                return False #sobreposição de peças
            else:
                mapa[linha][coluna+i]='N'
    
    elif orientacao=='v':
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if (linha+i)>len(mapa)-1:
                return False #peça fora do mapa
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if mapa[linha+i][coluna]=='N':
                return False #sobreposição de peças
            else:
                mapa[linha+i][coluna]='N'

    return True