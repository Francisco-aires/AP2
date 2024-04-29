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


print("BATALHA NAVAL INSPER")
print('\n')
print("Iniciando o jogo!")
print("O computador já está alocando os navios do país {0}...".format(random.choice(lista_paises)))

print("1: Brasil \n 1 cruzador \n 2 torpedeiro \n 1 destroyer \n 1 couracado \n 1 porta-avioes \n \n2: França \n 3 cruzador \n 1 porta-avioes \n 1 destroyer \n 1 couracado \n 1 submarino \n\n3: Austália \n 1 couracao \n 3 cruzador \n 1 submarino \n 1 torpedeiro \n 1 porta-avioes \n\n4: Rússia \n 1 cruzador \n 1 porta-avioes \n 2 couracado \n 1 destroyer \n 1 submarino \n\n5: Japão \n 2 torpedeiro \n 1 cruzador \n 2 destroyer \n 1 couracado \n 1 submarino")
print('\n')
n_nacao=0 #n_nacao= númerro da nação escolhida
while n_nacao!=1 and n_nacao!=2 and n_nacao!=3 and n_nacao!=4 and n_nacao!=5:
    n_nacao=int(input('Qual o número da nação da sua frota?'))
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

mapa_visivel=('''
    A B C D E F G H I J K
1  {}{}{}{}{}{}{}{}{}{}{}
2  {}{}{}{}{}{}{}{}{}{}{}
3  {}{}{}{}{}{}{}{}{}{}{}
4  {}{}{}{}{}{}{}{}{}{}{}
5  {}{}{}{}{}{}{}{}{}{}{}
6  {}{}{}{}{}{}{}{}{}{}{}
7  {}{}{}{}{}{}{}{}{}{}{}
8  {}{}{}{}{}{}{}{}{}{}{}
9  {}{}{}{}{}{}{}{}{}{}{}
10 {}{}{}{}{}{}{}{}{}{}{}
    A B C D E F G H I J K''')
