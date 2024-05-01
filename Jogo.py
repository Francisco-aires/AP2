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
# funçao para a cores
def cor(palavra,cor):
    if cor == 'red' or cor == 'vermelho':
        return ('\u001b[31m{0}\u001b[0m'.format(palavra))
    elif cor == 'blue' or cor == 'azul':
        return ('\u001b[34m{0}\u001b[0m'.format(palavra))
    elif cor == 'verde' or cor == 'green':
        return ('\u001b[32m{0}\u001b[0m'.format(palavra))
    elif cor == 'yellow' or cor == 'amarelo':
        return ('\u001b[33m{0}\u001b[0m'.format(palavra))
    else:
        return('cor {0} indisponivel'.format(cor))

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
                return ('Não foi possível colocar a peça nessa posição') #peça fora do mapa
    
        for i in range(0,n_blocos):#posição ocupada pelo bloco
            if mapa[linha][coluna+i]=='N':
                return ('Não foi possível colocar a peça nessa posição') #sobreposição de peças
            else:
                mapa[linha][coluna+i]='N'
    
    elif orientacao=='v':
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if (linha+i)>len(mapa)-1:
                return ('Não foi possível colocar a peça nessa posição') #peça fora do mapa
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if mapa[linha+i][coluna]=='N':
                return ('Não foi possível colocar a peça nessa posição') #sobreposição de peças
            else:
                mapa[linha+i][coluna]='N'
    return ('Navio colocado!')

def cria_mapa(dimensao):
    lista_mapa=[]
    for i in range (0,dimensao):
        lista_linha=[]
        for i in range (0,dimensao):
            lista_linha.append(' ')
        lista_mapa.append(lista_linha)
    return lista_mapa

dic_coluna = {
    'a': 0,
    'A': 0,
    'b': 1,
    'B': 1,   
    'c': 2,
    'C': 2,
    'd': 3,
    'D': 3,
    'e': 4,
    'E': 4,
    'f': 5,
    'F': 5,
    'g': 6,
    'G': 6,
    'h': 7,
    'H': 7,
    'I': 8,
    'i': 8,
    'J': 9,
    'j': 9
} #lista pra valores pras colunas no mapa
dic_n_linhas={'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9} #Dicionário para converter o número do tabuleiro (linha) no índice real da linha


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

#PRODUÇÃO DO TABULEIRO DO JOGO #####################################################
mapa_jogador=cria_mapa(10)
mapa_computador=cria_mapa(10)

def tabuleiro_jogo(mapa):
    i=1
    lista_colunas=['A','B','C','D','E','F','G','H','I','J']
    print('   '+' '.join(lista_colunas))
    for linha in mapa:
        print(f"{str(i):>2}"+' '+' '.join(linha))
        i+=1
    return('   '+' '.join(lista_colunas))
    

print("Computador- {0}".format(pais_computador))
print(tabuleiro_jogo(mapa_computador))
print("Jogador- {0}".format(pais_jogador))
print(tabuleiro_jogo(mapa_jogador))




#DISTRIBUIÇÃO PEÇAS PARA JOGADORES, POR PAÍS ESCOLHIDO############################
dic_frota_computador=PAISES[pais_computador] #frota do computador é um dicionário
lista_n_blocos_frota_computador=[] #para alocar os navios no mapa
for tipo_barco,quantidade in dic_frota_computador.items():
    for i in range(0,quantidade):
        lista_n_blocos_frota_computador.append(CONFIGURACAO[tipo_barco])


dic_frota_jogador=PAISES[pais_jogador] #frota de jogador é um dicionário
lista_n_blocos_frota_jogador=[] #para alocar os navios no mapa
lista_frota_jogador=[]
for tipo_barco,quantidade in dic_frota_jogador.items():
    for i in range(0,quantidade):
        lista_n_blocos_frota_jogador.append(CONFIGURACAO[tipo_barco])
        lista_frota_jogador.append(tipo_barco)


#ALOCAR PEÇAS###############################################
for i in range (0,len(lista_n_blocos_frota_jogador)):
    n_blocos=lista_n_blocos_frota_jogador[i]
    tipo_peca=lista_frota_jogador[i]
    print("alocar: {0} ({1} blocos)".format(tipo_peca,n_blocos))
    confirma_posicao='N'
    while confirma_posicao=='N':
        confirma_letra="N"
        confirma_linha="N"
        confirma_orientacao="N"
        while confirma_letra=="N":
            letra=input('Informe a letra: ')
            if letra in dic_coluna:
                confirma_letra="S"
                coluna=dic_coluna[letra]
            else:
                print("Letra inválida")
        
        while confirma_linha=="N":
            linha=input('Informe a linha: ')
            if linha in dic_n_linhas:
                confirma_linha="S"
                linha=dic_n_linhas[linha]
            else:
                print("Linha inválida")
        while confirma_orientacao=='N':   
            orientacao = input('Informe a Orientação [v | h]: ')
            if orientacao!='v' and orientacao!='h' and orientacao!='V' and orientacao!='H':
                print ("Orientação inválida")
            else:
                confirma_orientacao="S"
        posicao_peca=posicao_suporta(mapa_jogador,n_blocos,linha,coluna,orientacao)
        if posicao_peca=='Navio colocado!':
            confirma_posicao='S'
        elif posicao_peca=='Não foi possível colocar a peça nessa posição':
            confirma_posicao='N'
        print(posicao_peca)
        
        print("Computador- {0}".format(pais_computador))
        print(tabuleiro_jogo(mapa_computador))
        print("Jogador- {0}".format(pais_jogador))
        print(tabuleiro_jogo(mapa_jogador))