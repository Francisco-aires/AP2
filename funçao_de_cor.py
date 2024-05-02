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
    
def teste(z):
    if z == 'x':
        return 'uuuu'
    elif z == cor('x','verde'):
        return 'aaaaaa'
    
print(teste(cor('x','verde')))
    