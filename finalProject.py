         #-#-#-#-#-#-#-#-#-#-#
         #    Projeto 2      #
         #                   #
         #   Palavra GURU    #
         #   Multi Jogador   #
         #                   #
     #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
     #                               #
     #  Nome: Paulo Neves Alexandre  #
     #  Numero: 90761                #
     #  Curso: LEIC-T                #
     #                               #
     #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

              
#-#-#-#-#-#-#-#-#-#-#-#     INICIO DO CODIGO     #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#



from parte1 import e_palavra
import itertools



           #-----------T.A.D. palavra_potencial----------------#
           #                                                   #
           #  Um elemento do tipo palavra_potencial            #
           #  e representado por uma cadeia de carateres       #
           #  em que todos os carateres sao letras maiusculas. #
           #                                                   #  
           #---------------------------------------------------#



#---------------------------------CONSTRUTOR------------------------------------



def cria_palavra_potencial(palavra,tuplo):
    """ cria_palavra_potencial: str x tuplo -> palavra_potencial
        cria_palavra_potencial(palavra,tuplo) devolve uma palavra com todas
        as letras maiusculas, pertencentes obrigatoriamente ao tuplo,
        ocorre erro(argumentos invalidos) no caso de cada um dos carateres 
        tanto do tuplo como da palavra nao serem letras maiusculas, ou erro
        (palavra nao valida) no caso das letras da palavra nao pertencerem
        ao tuplo."""
    
    
    if  not isinstance(palavra,str) or not isinstance(tuplo,tuple):
        raise ValueError("cria_palavra_potencial:argumentos invalidos.")
 
    
    for i in tuplo:
        if not isinstance(i,str) or len(i)!=1:
            raise ValueError("cria_palavra_potencial:argumentos invalidos.")
   
    
    for i in palavra:
        if not ord("A")<=ord(i)<=ord("Z"):
            raise ValueError("cria_palavra_potencial:argumentos invalidos.")

    
    for i in tuplo:
        if not ord("A")<=ord(i)<=ord("Z"):
            raise ValueError("cria_palavra_potencial:argumentos invalidos.") 

    
    if len(palavra)>len(tuplo):
        raise ValueError("cria_palavra_potencial:a palavra nao e valida.")
    
    #  Cria uma lista com os elementos do tuplo
    l_letras=[]
    for i in tuplo:
        l_letras.append(i)
    
    # Para todos os carateres da palavra, verifica se esta na lista, e remove-o
    for a in palavra:  
        if a in l_letras:
            l_letras.remove(a)
        else:
            raise ValueError("cria_palavra_potencial:a palavra nao e valida.")
    
    
    return palavra



#---------------------------------SELETOR--------------------------------------#



def palavra_tamanho(palavra_potencial):
    ''' palavra_tamanho : palavra_potencial -> int
        palavra_tamanho(palavra_potencial) devolve o numero de letras da palavra.'''
    
    
    return len(palavra_potencial)



#--------------------------------VERIFICADOR-----------------------------------#



def e_palavra_potencial(universal):
    ''' e_palavra_potencial : universal -> logico
        e_palavra_potencial(universal) devolve True caso o argumento seja do
        tipo palavra_potencial, False em caso contrario. '''
    
    
    if not isinstance(universal,str):
        return False
    
    for i in universal:
        
        if not ord("A")<=ord(i)<=ord("Z"):
            return False
    
    return True



#----------------------------------TESTES--------------------------------------#



def palavras_potenciais_iguais(pp,pp1):
    ''' palavras_potenciais_iguais : palavra_potencial x palavra_potencial -> logico
        palavras_potenciais_iguais(pp,pp1) devolve True caso as palavras 
        potenciais sejam iguais, False em caso contrario'''
    
    
    if pp==pp1:
        return True
    
    return False


def palavra_potencial_menor(pp,pp1):
    ''' palavra_potencial_menor : palavra_potencial x palavra_potencial -> logico
        palavra_potencial_menor(pp,pp1) devolve True no caso de pp ser 
        alfabeticamente anterior a pp1, False em caso contrario'''
    
    
    if pp==pp1:
        return False
    
    i=0
    
    # Soma 1 ao contador enquanto as letras das palavras forem iguais
    while pp[i]==pp1[i]:
        i+=1
    
    # Verifica qual das primeiras letras diferentes nas duas palavras e menor alfabeticamente
    if ord(pp[i])<ord(pp1[i]):
        return True
    
    return False



#-------------------------------TRANSFORMADOR----------------------------------#



def palavra_potencial_para_cadeia(pp):
    '''palavra_potencial_menor : palavra_potencial -> str
       palavra_potencial_menor(pp) devolve uma cadeia de carateres
       a representar a pp.'''
  
    
    return pp



#--------------------FIM T.A.D palavra_potencial-------------------------------#
           
           
           
           #-----------T.A.D. conjunto_palavras-----------#
           #                                              #
           #   Um elemento do tipo conjunto_palavras      #
           #   e representado por uma lista que guarda    #
           #   palavras_potenciais.                       #
           #                                              #
           #----------------------------------------------#



#---------------------------------CONSTRUTOR-----------------------------------#



def cria_conjunto_palavras():
    '''cria_conjunto_palavras:    ->conjunto_palavras
       cria_conjunto_palavras() devolve um conjunto de palavras vazio.'''
    
    
    return []



#----------------------------------SELETOR-------------------------------------#



def numero_palavras(conjunto):
    '''numero_palavras: conjunto_palavras->int
       numero_palavras(conjunto) devolve um inteiro correspondente
       ao numero de palavras no conjunto.'''

    
    return len(conjunto)



#--------------------------------MODIFICADORES---------------------------------#



def subconjunto_por_tamanho(conjunto,n):
    '''subconjunto_por_tamanho: conjunto_palavras x int -> list
       subconjunto_por_tamanho(conjunto,n) devolve uma lista com 
       as palavras_potenciais de tamanho n contidas no conjunto_palavras.'''

    
    subconjunto=[]
    
    for i in conjunto:
        
        if len(i)==n:
            subconjunto.append(i)
    
    subconjunto.sort()
    
    return subconjunto


def acrescenta_palavra(conjunto,pp):
    ''' acrescenta_palavra: conjunto_palavras x palavra_potencial -> 
        acrescenta_palavra(conjunto,pp) nao da return em nada, apenas 
        junta a palavra pp ao conjunto.'''

    
    if e_palavra_potencial(pp)==False or e_conjunto_palavras(conjunto)==False:
        raise ValueError("acrescenta_palavra:argumentos invalidos.")
    
    if pp not in conjunto:
        conjunto.append(pp)



#----------------------------------VERIFICADOR---------------------------------#      



def e_conjunto_palavras(universal):
    ''' e_conjunto_palavras: universal -> logico
        e_conjunto_palavras(universal) devolve True caso o argumento
        seja do tipo conjunto_palavras, False em caso contrario'''


    if not isinstance(universal,list):
        return False
    
    for i in universal:
        
        if e_palavra_potencial(i)==False:
            return False
    
    return True



#-------------------------------------TESTE------------------------------------# 



def conjuntos_palavras_iguais(l1,l2):
    '''conjuntos_palavras_iguais: conjunto_palavras x conjunto_palavras -> logico
       conjuntos_palavras_iguais(l1,l2) devolve True caso os dois conjuntos_palavras
       contenham as mesmas palavras, False em contrario.'''

    
    if numero_palavras(l1)!=numero_palavras(l2):
        return False
    
    # Criacao de uma lista igual a l2, para nao haver mudancas em l2
    l4=l2[:]
    
    for i in l1:
        if i not in l4:
            return False
        l4.remove(i)      
    
    return True



#------------------------------TRANSFORMADOR-----------------------------------#



def conjunto_palavras_para_cadeia(conj):
    '''conjuntos_palavras_para_cadeia: conjunto_palavras -> str
       conjuntos_palavras_para_cadeia(conj) devolve uma cadeia de carateres
       que representa o conjunto, por ordem crescente de tamanho e alfabeticamente.'''

    
    n=0
    cadeia=""
    
    for i in conj:
        if len(i)>n:
            n=len(i)
    
    for i in range(n,-1,-1):
        if subconjunto_por_tamanho(conj,i)!=[]: 
            
            if i==n:
                cadeia=str(i)+"->"+"["+str(", ".join(subconjunto_por_tamanho(conj,i)))+"]"+cadeia
            else:
                cadeia=str(i)+"->"+"["+str(", ".join(subconjunto_por_tamanho(conj,i)))+"]"+";"+cadeia
    
    return "["+cadeia+"]"

#----------------------------FIM T.A.D conjunto_palavras-----------------------#



           #--------------------T.A.D. jogador---------------#
           #                                                 #
           #  Um elemento do tipo jogador e representado     #
           #  por uma lista que guarda o nome, a pontuacao,  #
           #  a lista das palavras validas e a lista das     #
           #  palavras invalidas.                            #
           #                                                 #
           #-------------------------------------------------#



#---------------------------------CONSTRUTOR------------------------------------



def cria_jogador(nome):
    ''' cria_jogador: str -> jogador
        cria_jogador(nome) devolve uma lista com o nome, pontuacao a 0,
        lista vazia de palavras validas e lista vazia de palavras invalidas'''
    
    
    if not isinstance(nome,str):
        raise ValueError("cria_jogador:argumento invalido.")
    
    return [nome,0,cria_conjunto_palavras(),cria_conjunto_palavras()]



#--------------------------------SELETORES-------------------------------------#



def jogador_nome(jog):
    '''jogador_nome: jogador -> str
       jogador_nome(jog) devolve o nome do jogador.'''
    
    
    return jog[0]


def jogador_pontuacao(jog):
    '''jogador_pontuacao: jogador -> int
       jogador_pontuacao(jog) devolve a pontuacao do jogador ate ao momento.'''
    
    
    return jog[1]


def jogador_palavras_validas(jog):
    '''jogador_palavras_validas: jogador -> conjunto_palavras
       jogador_palavras_validas(jog) devolve um conjunto de palavras validas propostas
       pelo jogador ate ao momento.'''
    
    
    return jog[2]


def jogador_palavras_invalidas(jog):
    '''jogador_palavras_invalidas: jogador -> conjunto_palavras
       jogador_palavras_invalidas(jog) devolve um conjunto de palavras invalidas 
       propostas pelo jogador ate ao momento.'''  
    
    
    return jog[3]



#------------------------------MODIFICADORES-----------------------------------#



def adiciona_palavra_valida(jog,p):
    '''adiciona_palavra_valida: jogador x palavra_potencial -> 
       adiciona_palavra_valida(jog,p) tem como efeito adicionar a palavra_potencial
       ao conjunto de palavras validas propostas pelo jogador e atualiza a pontuacao
       do jogador.'''
    
    
    if e_palavra_potencial(p)==False or e_jogador(jog)==False:
        raise ValueError("adiciona_palavra_valida:argumentos invalidos.") 
    
    if p not in jogador_palavras_validas(jog):
        acrescenta_palavra(jogador_palavras_validas(jog),p)
        jog[1]=jogador_pontuacao(jog)+palavra_tamanho(p)
    

def adiciona_palavra_invalida(jog,p):
    '''adiciona_palavra_invalida: jogador x palavra_potencial -> 
       adiciona_palavra_invalida(jog,p) tem como efeito adicionar a palavra_potencial
       ao conjunto de palavras invalidas propostas pelo jogador e atualiza a pontuacao
       do jogador.'''     
    
    
    if e_palavra_potencial(p)==False or e_jogador(jog)==False:
        raise ValueError("adiciona_palavra_invalida:argumentos invalidos.")    
    
    if p not in jogador_palavras_invalidas(jog):
        acrescenta_palavra(jogador_palavras_invalidas(jog),p)
        jog[1]=jogador_pontuacao(jog)-palavra_tamanho(p)



#----------------------------------VERIFICADOR---------------------------------#



def e_jogador(univ):
    '''e_jogador: universal -> logico
       e_jogador(univ) devolve True caso o argumento seja do tipo jogador,
       False em caso contrario.'''
    
    
    if isinstance(univ,list) and len(univ)==4 \
       and isinstance(univ[0],str) and isinstance(univ[1],int) \
       and e_conjunto_palavras(univ[2])==True\
       and e_conjunto_palavras(univ[3])==True:
        
        return True
    
    return False



#------------------------------TRANSFORMADOR-----------------------------------#



def jogador_para_cadeia(jog):
    ''' jogador_para_cadeia: jogador -> str
        jogador_para_cadeia(jog) devolve uma cadeia de carateres que representa
        o jogador, pelo seu nome, pontuacao, palavras validas propostas 
        e palavras invalidas propostas.'''
    
    return "JOGADOR " + jogador_nome(jog) + " PONTOS="+ str(jogador_pontuacao(jog)) \
           + " VALIDAS=" + conjunto_palavras_para_cadeia(jogador_palavras_validas(jog)) \
           + " INVALIDAS="+conjunto_palavras_para_cadeia(jogador_palavras_invalidas(jog))



#----------------------------FIM T.A.D jogador---------------------------------#



           #--------------------------------------------------#
           #   FUNCAO ADICIONAL - GERA_TODAS_PALAVRAS_VALIDAS #
           #                                                  #
           #  Esta funcao gera todas as palavras validas de   #
           #  acordo com a gramatica, a partir das letras do  #
           #  tuplo usado como argumento.                     #
           #                                                  #
           #--------------------------------------------------#



def gera_todas_palavras_validas(tuplo):
    '''gera_todas_palavras_validas: tuplo -> conjunto_palavras
       gera_todas_palavras_validas(tuplo) devolve um conjunto_palavras contendo
       as palavras validas de acordo com a gramatica.'''
   
   
        #  GERADOR DE TODAS AS PERMUTACOES POSSIVEIS A PARTIR DO TUPLO  #
    
    permutacoes=()
    
    for i in range(len(tuplo),0,-1):
        for palavra_permutada in itertools.permutations(tuplo,i):
            permutacoes=permutacoes+("".join(palavra_permutada),) 
    
    
    #  CRIACAO DE UMA LISTA COM AS PALAVRAS VALIDAS ATRAVES DA GRAMATICA  #
    
    palavras_validas=cria_conjunto_palavras()
    
    for palavra in permutacoes:
        
        if e_palavra(palavra)==True:
            acrescenta_palavra(palavras_validas,(cria_palavra_potencial(palavra,tuplo)))
    
    return palavras_validas



           #--------------------------------------------------#
           #            FUNCAO ADICIONAL - GURU_MJ            #
           #                                                  #
           #  Esta funcao permite jogar um jogo completo do   #
           #  jogo Palavra Guru Multijogador.                 #
           #                                                  #
           #                                                  #
           #--------------------------------------------------#



def guru_mj(tuplo):
    '''guru_mj: tuplo -> 
       guru_mj(tuplo) recebe um tuplo correspondente ao conjunto de letras usadas 
       na formacao das palavras em jogo (O tuplo deve ser constituido por letras 
       maiusculas), e apresenta no final uma mensagem do jogador vencedor ou de 
       empate, no caso de existir mais de um jogador com melhor pontuacao.'''
    
    print("Find all the portuguese words from :")
    
    print (tuplo)      
    
    print("Introduce the name of the players (-1 to stop)...")
    
        # Pedido do nome do jogador e criacao de uma lista de jogadores #

    n=1
    nome=""
    lista_jogadores=[]
    
    while nome!="-1":
        nome = input("PLAYER "+ str(n) +" -> ")
        
        if nome!="-1":
            lista_jogadores.append(nome)
        n+=1 
    
    for i in range(len(lista_jogadores)):
        lista_jogadores[i]=cria_jogador(lista_jogadores[i])
    
   # Apresentacao das jogadas enquanto existem palavras validas para acertar #
    
    n=0
    palavras_validas=gera_todas_palavras_validas(tuplo)
    palavras_jogadas=cria_conjunto_palavras()
    
    while len(palavras_validas)!=len(palavras_jogadas):
        
        for i in range(len(lista_jogadores)):
            n+=1
            if len(palavras_validas)!=len(palavras_jogadas):  
                print ("PLAY "+str(n) + " - " + str(len(palavras_validas)-len(palavras_jogadas)) + " words to discover.")
                palavra_jogada=palavra_potencial_para_cadeia(cria_palavra_potencial(input("PLAYER " + jogador_nome(lista_jogadores[i])+" -> "),tuplo))
                
                if e_palavra(palavra_jogada)==True:
                    print(palavra_jogada + " - VALID word")
                    if palavra_jogada not in palavras_jogadas:
                        adiciona_palavra_valida(lista_jogadores[i],palavra_jogada)
                        acrescenta_palavra(palavras_jogadas,palavra_jogada)
                
                else:
                    print(palavra_jogada + " - INVALID word")
                    adiciona_palavra_invalida(lista_jogadores[i],palavra_jogada)
    
                # Verificacao da melhor pontuacao do jogo #
    
    pontuacao_jogadores=[]
    
    for i in lista_jogadores:
        pontuacao_jogadores.append(jogador_pontuacao(i))
    
    melhor_pontuacao=max(pontuacao_jogadores)
    
           # Apresentacao da mensagem final, consoante os resultados #
    
    jogadores_vencedores=[]
    
    for i in lista_jogadores:
        if jogador_pontuacao(i)==melhor_pontuacao:
            jogadores_vencedores.append(i)
    
    if len(jogadores_vencedores)==1:
        print("END OF THE GAME! The game ended up with a victory of " + \
              jogador_nome(jogadores_vencedores[0])+ " with " + \
              str(jogador_pontuacao(jogadores_vencedores[0])) + " points.")
    
    elif len(jogadores_vencedores)>1:
        print ("END OF THE GAME! The game ended in a draw.")
    
    for i in lista_jogadores:
        print (jogador_para_cadeia(i))


letters = input("Please insert the letters (in capital letters) you want to play with : ")
guru_mj(tuple(letters))