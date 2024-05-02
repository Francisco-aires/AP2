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
        if '▓' in linha:
            return False
    return True

def is_numero(string):
    return string.isdigit()

import time
#contagem regressiva
def contagem_regressiva(tempo):
    for i in range(tempo, 0, -1):
        print(i)
        time.sleep(1)

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
                        if mapa[linha][coluna+i]=='▓':
                            aloca=-1  #sobreposição de peças
                        i+=1
                        
                if aloca==0: #quer dizer que é possível alocar o barco (já que aloca não é false)
                    for i in range(0,n_blocos):
                        mapa[linha][coluna+i]='▓'
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
                        if mapa[linha+i][coluna]=='▓':
                            aloca=-1 #sobreposição de peças
                        i+=1
                if aloca==0:  #quer dizer que é possível alocar o barco (já que aloca não é false)
                    for i in range(0,n_blocos):
                        mapa[linha+i][coluna]='▓'
                    aloca='positivo'
    
    return mapa 

def posicao_suporta(mapa, n_blocos, linha, coluna, orientacao):
    if orientacao == 'h':
        for i in range(0, n_blocos):  # posição ocupada pelo bloco
            if coluna + i > len(mapa[linha]) - 1 or mapa[linha][coluna + i] != ' ':
                return 'Não foi possível colocar a peça nessa posição'  # peça fora do mapa ou sobreposição de peças
            else:
                mapa[linha][coluna + i] = cor('▓', 'verde')
    elif orientacao == 'v':
        for i in range(0, n_blocos):  # posição ocupada pelo bloco
            if linha + i > len(mapa) - 1 or mapa[linha + i][coluna] != ' ':
                return 'Não foi possível colocar a peça nessa posição'  # peça fora do mapa ou sobreposição de peças
            else:
                mapa[linha + i][coluna] = cor('▓', 'verde')
    return 'Navio colocado!'

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
print('O computador ja esta em posiçâo de batalha!')

print("1: Brasil \n 1 cruzador \n 2 torpedeiro \n 1 destroyer \n 1 couracado \n 1 porta-avioes \n \n2: França \n 3 cruzador \n 1 porta-avioes \n 1 destroyer \n 1 couracado \n 1 submarino \n\n3: Austália \n 1 couracao \n 3 cruzador \n 1 submarino \n 1 torpedeiro \n 1 porta-avioes \n\n4: Rússia \n 1 cruzador \n 1 porta-avioes \n 2 couracado \n 1 destroyer \n 1 submarino \n\n5: Japão \n 2 torpedeiro \n 1 cruzador \n 2 destroyer \n 1 couracado \n 1 submarino")
print('\n')
n_nacao=0 #n_nacao= númerro da nação escolhida
pais_jogador=lista_paises[n_nacao-1]

#COLOCANDO COORDENADAS PARA JOGADOR POSICIONAR O NAVIO #################
while True:
    n_nacao = input('Qual o número da nação da sua frota? ')
    if is_numero(n_nacao):
        n_nacao = int(n_nacao)
        if 1 <= n_nacao <= 5:
            pais_jogador = lista_paises[n_nacao-1]
            print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
            break  # Sai do loop se a entrada for válida
        else:
            print('Opção inválida. Escolha um número de 1 a 5.')
    else:
        print('Opção inválida. Digite um número inteiro.')
print("Agora é vez de alocar seus navios de guerra!")

#PRODUÇÃO DO TABULEIRO DO JOGO #####################################################
mapa_jogador=cria_mapa(10)
mapa_computador=cria_mapa(10)
mapa_fantasma=cria_mapa(10)

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
print('\n')
print("Jogador- {0}".format(pais_jogador))
print(tabuleiro_jogo(mapa_jogador))




#DISTRIBUIÇÃO PEÇAS PARA JOGADORES, POR PAÍS ESCOLHIDO############################
dic_frota_computador = PAISES[pais_computador]  # Frota do computador é um dicionário
lista_n_blocos_frota_computador = []  # Para alocar os navios no mapa
for tipo_barco, quantidade in dic_frota_computador.items():
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
    confirma_posicao='N'
    while confirma_posicao=='N':
        print("alocar: {0} ({1} blocos)".format(tipo_peca,n_blocos))
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
        posicao_peca_jogador=posicao_suporta(mapa_jogador,n_blocos,linha,coluna,orientacao)
        if posicao_peca_jogador=='Navio colocado!':
            confirma_posicao='S'
        elif posicao_peca_jogador=='Não foi possível colocar a peça nessa posição':
            confirma_posicao='N'
        print(posicao_peca_jogador)
        
        print("Computador- {0}".format(pais_computador))
        print(tabuleiro_jogo(mapa_fantasma))
        print('\n')
        print("Jogador- {0}".format(pais_jogador))
        print(tabuleiro_jogo(mapa_jogador))


posicao_peca_computador=aloca_navios(mapa_computador,lista_n_blocos_frota_computador)


print('Iniciando a batalha naval!')
contagem_regressiva(5)

print("Computador- {0}".format(pais_computador))
print(tabuleiro_jogo(mapa_fantasma))
print('\n')
print("Jogador- {0}".format(pais_jogador))
print(tabuleiro_jogo(mapa_jogador))

#função ataque computador
def ataque_computador(mapa_jogador):
    condicao_ataque=0 #condição incial
    while condicao_ataque==0:
        linha_atacada=random.randint(0,9)
        coluna_atacada=random.randint(0,9)
        if mapa_jogador[linha_atacada][coluna_atacada]=='A' or mapa_jogador[linha_atacada][coluna_atacada]=='X': #ou seja esse ponto já foi atacado
            condicao_ataque=0
        elif mapa_jogador[linha_atacada][coluna_atacada]==' ':
            condicao_ataque=1 #ou seja o ataque foi realizado
            mapa_jogador[linha_atacada][coluna_atacada]=cor('▓', 'azul') #nesse caso o ataque atingiu a água #trocar pela caixa azul
            print('Computador -------->>>>>>>    {0}{1}    Água!'.format(coluna_atacada,linha_atacada))
        else:
            condicao_ataque=1 #ataque realizado
            mapa_jogador[linha_atacada][coluna_atacada]=cor('▓', 'vermelho') # nesse caso o ataque atingiu uma embarcação #trocar x por caixa vermelha
            print ('Computador -------->>>>>>>    {0}{1}    BOOOOOMMMMMMMMM!!!!!!!!!!'.format(coluna_atacada,linha_atacada))

#função ataque jogador:
def ataque_jogador(mapa_computador,linha_atacada_jogador,n_coluna_atacada_jogador,coluna_atacada_jogador,condicao_ataque):
    condicao_ataque=0 #condição incial
    if mapa_computador[linha_atacada_jogador][n_coluna_atacada_jogador]=='A' or mapa_computador[linha_atacada_jogador][n_coluna_atacada_jogador]=='X': #ou seja esse ponto já foi atacado
        condicao_ataque=0
        print('Posição {0}{1} já foi bombardeada!'.format(coluna_atacada_jogador,linha_atacada_jogador))
    elif mapa_computador[linha_atacada_jogador][n_coluna_atacada_jogador]==' ':
        condicao_ataque=1 #ou seja o ataque foi realizado
        mapa_computador[linha_atacada_jogador][n_coluna_atacada_jogador]='A' #nesse caso o ataque atingiu a água
        mapa_fantasma[linha_atacada_jogador][n_coluna_atacada_jogador]=cor('▓', 'azul')
        print('Jogador -------->>>>>>>    {0}{1}    Água!'.format(coluna_atacada_jogador,linha_atacada_jogador))
    else:
        condicao_ataque=1 #ataque realizado
        mapa_computador[linha_atacada_jogador][n_coluna_atacada_jogador]='X' # nesse caso o ataque atingiu uma embarcação
        mapa_fantasma[linha_atacada_jogador][n_coluna_atacada_jogador]=cor('▓', 'vermelho')
        print ('Jogador -------->>>>>>>    {0}{1}    BOOOOOMMMMMMMMM!!!!!!!!!!'.format(coluna_atacada_jogador,linha_atacada_jogador))



#Sorteio início partida#############
primeiro_a_jogar=random.randint(0,1)
if primeiro_a_jogar==0: #computador inicia
    while foi_derrotado(mapa_computador)==False and foi_derrotado(mapa_jogador)==False:
        print(ataque_computador(mapa_jogador))
        print("Computador- {0}".format(pais_computador))
        print(tabuleiro_jogo(mapa_fantasma))
        print('\n')
        print("Jogador- {0}".format(pais_jogador))
        print(tabuleiro_jogo(mapa_jogador))
        print("Coordenadas do seu disparo")
        while True:
            coluna_atacada_jogador=input('Letra:')
            if is_numero(coluna_atacada_jogador):
                    print('Opção inválida. Digite uma letra.')
            else: 
                    if  coluna_atacada_jogador in dic_coluna:
                        n_coluna_atacada_jogador=dic_coluna[coluna_atacada_jogador]
                        break  # Sai do loop se a entrada for válida
                    else:
                        print('Opção inválida. Escolha uma letra de A a J.')
        while True:
            linha_atacada_jogador=input("Linha:")
            if is_numero(linha_atacada_jogador):
                    linha_atacada_jogador= int(linha_atacada_jogador)
                    if 1 <= linha_atacada_jogador <= 10:
                        linha_atacada_jogador-=1
                        break  # Sai do loop se a entrada for válida
                    else:
                        print('Opção inválida. Escolha um número de 1 a 10.')
            
            else:
                print('Opção inválida. Digite um número inteiro.')
        print(ataque_jogador(mapa_computador,linha_atacada_jogador,n_coluna_atacada_jogador,coluna_atacada_jogador))

        


else: #jogador incia
    while foi_derrotado(tabuleiro_jogo(mapa_computador))==False and foi_derrotado(tabuleiro_jogo(mapa_jogador))==False:
        print("Coordenadas do seu disparo")
        while True:
            coluna_atacada_jogador=input('Letra:')
            if is_numero(coluna_atacada_jogador):
                    print('Opção inválida. Digite uma letra.')
            else: 
                    if  coluna_atacada_jogador in dic_coluna:
                        n_coluna_atacada_jogador=dic_coluna[coluna_atacada_jogador]
                        break  # Sai do loop se a entrada for válida
                    else:
                        print('Opção inválida. Escolha uma letra de A a J.')
        while True:
            linha_atacada_jogador=input("Linha:")
            if is_numero(linha_atacada_jogador):
                    linha_atacada_jogador= int(linha_atacada_jogador)
                    if 1 <= linha_atacada_jogador <= 10:
                        linha_atacada_jogador-=1
                        break  # Sai do loop se a entrada for válida
                    else:
                        print('Opção inválida. Escolha um número de 1 a 10.')
            else:
                print('Opção inválida. Digite um número inteiro.')
            print(ataque_jogador(mapa_computador,linha_atacada_jogador,n_coluna_atacada_jogador,coluna_atacada_jogador))
            print(ataque_computador(mapa_jogador))
            print("Computador- {0}".format(pais_computador))
            print(tabuleiro_jogo(mapa_fantasma))
            print('\n')
            print("Jogador- {0}".format(pais_jogador))
            print(tabuleiro_jogo(mapa_jogador))


