import random

# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
PAISES =  {'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}
def foi_derrotado(matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True
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
def cria_mapa(dimensao):
    lista_mapa=[]
    lista_linha=[]
    for i in range (0,dimensao):
           lista_linha.append(' ')
    for i in range (0,dimensao):
        lista_mapa.append(lista_linha)
    return lista_mapa



lista_paises=[]
for pais in PAISES:
    lista_paises.append(pais)

pais_computador=random.choice(lista_paises)
print("BATALHA NAVAL INSPER")
print('\n')
print("Iniciando o jogo!")
print("O computador já está alocando os navios do país {0}...".format(pais_computador))

print("1: Brasil \n 1 cruzador \n 2 torpedeiro \n 1 destroyer \n 1 couracado \n 1 porta-avioes \n \n2: França \n 3 cruzador \n 1 porta-avioes \n 1 destroyer \n 1 couracado \n 1 submarino \n\n3: Austália \n 1 couracao \n 3 cruzador \n 1 submarino \n 1 torpedeiro \n 1 porta-avioes \n\n4: Rússia \n 1 cruzador \n 1 porta-avioes \n 2 couracado \n 1 destroyer \n 1 submarino \n\n5: Japão \n 2 torpedeiro \n 1 cruzador \n 2 destroyer \n 1 couracado \n 1 submarino")
print('\n')
n_nacao=0 #n_nacao= númerro da nação escolhida
pais_jogador=lista_paises[n_nacao-1]
while n_nacao!=1 and n_nacao!=2 and n_nacao!=3 and n_nacao!=4 and n_nacao!=5:
    n_nacao=int(input('Qual o número da nação da sua frota?'))
    pais_jogador=lista_paises[n_nacao-1]
    if n_nacao==1:
        print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
    elif n_nacao==2:
        print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
    elif n_nacao==3:
        print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
    elif n_nacao==4:
        print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
    elif n_nacao==5:
        print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
    else:
        print('Opção inválida')
print("Agora é vez de alocar seus navios de guerra!")

mapa=cria_mapa(10)
mapa_jogador=mapa
mapa_computador=mapa


def tabuleiro_jogo(mapa):
    i=1
    lista_colunas=['A','B','C','D','E','F','G','H','I','J']
    print('   '+' '.join(lista_colunas))
    for linha in mapa:
        print(f"{str(i):>2}"+' '+' '.join(linha))
        i+=1
    print('   '+' '.join(lista_colunas))

print("Computador- {0}".format(pais_computador))
print(tabuleiro_jogo(mapa_computador))
print("Jogador- {0}".format(pais_jogador))
print(tabuleiro_jogo(mapa_jogador))













