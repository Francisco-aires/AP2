print('\u001b[31m▓▓	█\u001b[0m')
#while n_nacao!=1 and n_nacao!=2 and n_nacao!=3 and n_nacao!=4 and n_nacao!=5:
 #   n_nacao=input('Qual o número da nação da sua frota?')
    #if is_numero(n_nacao):
     #   n_nacao = int(n_nacao)
      #  pais_jogador=lista_paises[n_nacao-1]
       # if n_nacao==1:
        
        #    print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
      #  elif n_nacao==2:
       
       #     print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
        #elif n_nacao==3:
      
        #    print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
        #elif n_nacao==4:
      
         #   print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))
        #elif n_nacao==5:
         #   print("Você escolheu a nação {0}".format(lista_paises[n_nacao-1]))    
        #else:
         #   print('Opção inválida')
   # else:
    #    print('Opção inválida')
def posicao_suporta(mapa,n_blocos,linha,coluna,orientacao):
    if orientacao=='h':
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if (coluna+i)>len(mapa[linha])-1:
                return ('Não foi possível colocar a peça nessa posição') #peça fora do mapa
    
        for i in range(0,n_blocos):#posição ocupada pelo bloco
            if mapa[linha][coluna+i]=='▓':
                return ('Não foi possível colocar a peça nessa posição') #sobreposição de peças
            else:
                mapa[linha][coluna+i]=cor('▓','verde')
    
    elif orientacao=='v':
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if (linha+i)>len(mapa)-1:
                return ('Não foi possível colocar a peça nessa posição') #peça fora do mapa
        for i in range(0,n_blocos): #posição ocupada pelo bloco
            if mapa[linha+i][coluna]=='▓':
                return ('Não foi possível colocar a peça nessa posição') #sobreposição de peças
            else:
                mapa[linha+i][coluna]=cor('▓','verde')
    return ('Navio colocado!')
