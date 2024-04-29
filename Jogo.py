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


lista_paises=[]
for pais in PAISES:
    lista_paises.append(pais)


print("BATALHA NAVAL INSPER")
print('\n')
print("Iniciando o jogo!")
print("O computador já está alocando os navios do país {0}...".format(random.choice(lista_paises)))

print("1: Brasil \n 1 cruzador \n 2 torpedeiro \n 1 destroyer \n 1 couracado \n 1 porta-avioes \n \n2: França \n 3 cruzador \n 1 porta-avioes \n 1 destroyer \n 1 couracado \n 1 submarino \n\n3: Austália \n 1 couracao \n 3 cruzador \n 1 submarino \n 1 torpedeiro \n 1 porta-avioes \n\n4: Rússia \n 1 cruzador \n 1 porta-avioes \n 2 couracado \n 1 destroyer \n 1 submarino \n\n5: Japão \n 2 torpedeiro \n 1 cruzador \n 2 destroyer \n 1 couracado \n 1 submarino")
print('\n')
input('Qual o número da nação da sua frota?')    

