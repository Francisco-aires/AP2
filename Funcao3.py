import random
def aloca_navios(mapa,lista_n_blocos):
    n_colunas=len(mapa[0])-1
    for n_blocos in lista_n_blocos:
        aloca=0 #aloca==0 é a condição incial do aloca
        while aloca==-1 or aloca==0: #aloca== -1, significa que esse é impossível de ser implementado
            linha = random.randint(0, len(mapa)-1)
            coluna = random.randint(0, n_colunas)
            orientacao = random.choice(['h', 'v'])
            i=0
            aloca=0
            if orientacao=='h':
                while aloca==0 and i<n_blocos: #posição ocupada pelo bloco while aloca==0 and i<n_blocos
                    if (coluna+i)>len(mapa[linha])-1:
                        aloca=-1 #peça fora do mapa
                    i+=1
                if aloca==0:
                    i=0
                    while aloca==0 and i<n_blocos:#posição ocupada pelo bloco
                        if mapa[linha][coluna+i]=='N':
                            aloca=-1  #sobreposição de peças
                        i+=1
                        
                if aloca==0: #quer dizer que é possível alocar o barco (já que aloca não é false)
                    for i in range(0,n_blocos):
                        mapa[linha][coluna+i]='N'
                    aloca='positivo'
            
            elif orientacao=='v':
                i=0
                while aloca==0 and i<n_blocos: #posição ocupada pelo bloco
                    if (linha+i)>len(mapa)-1:
                        aloca=-1 #peça fora do mapa
                    i+=1
                if aloca==0:
                    i=0
                    while aloca==0 and i<n_blocos: #posição ocupada pelo bloco (ver se é possível o bloco ocupar essa posição)
                        if mapa[linha+i][coluna]=='N':
                            aloca=-1 #sobreposição de peças
                        i+=1
                if aloca==0:  #quer dizer que é possível alocar o barco (já que aloca não é false)
                    for i in range(0,n_blocos):
                        mapa[linha+i][coluna]='N'
                    aloca='positivo'
    
    return mapa 