#Projeto 1 -          Gramatica Guru      -  Fundamentos de Programacao 
# Realizado por Paulo Neves Alexandre , numero:90761

#Inicio das linhas de codigo 


def tuplo_letras(tuplo,a):
    """
    funcao que adiciona letras a todos os elementos de um tuplo
    
    tuplo: tuple --> tuplo com os elementos a adicionar as letras
    a: str --> letras a adicionar
    return: tuple --> novo tuplo ja com as letras adicionadas
    """
    tuplo_letra=()
    for i in range(len(tuplo)):
        tuplo_letra=tuplo_letra +(tuplo[i]+a,)
    return tuplo_letra



def tuplos(t1,t2):
    """
    funcao que faz a juncao dos elementos de um tuplo a todos os elementos do outro, de maneira distributiva
    
    t1: tuple --> tuplo a que se vai adicionar os elementos 
    t2: tuple --> tuplo com os elementos a adicionar ao outro
    return : tuple --> novo tuplo ja com as operacoes realizadas
    """
    newTuple=()
    for a in range(len(t1)):       
        for i in range(len(t2)):
            newTuple=newTuple+(t1[a]+(t2[i]),)
        a+=1     
    return newTuple


# inicio da definicao da gramatica em si, com variaveis

art_def=("A","O")


vogal_palavra=(art_def) + ("E",)


vogal=("I","U",) + vogal_palavra


dit_palavra=("AI","AO","EU","OU")


dit=("AE","AU","EI","OE","OI","IU") + dit_palavra

   
par_vogal=dit+("IA","IO")


cons_freq=("D","L","M","N","P","R","S","T","V")


cons_term=("L","M","R","S","X","Z")


cons_final=("N","P") + cons_term


cons=("B","C","D","F","G","H","J","L","M","N","P","Q","R","S","T","V","X","Z")


par_cons=("BR","CR","FR","GR","PR","TR","VR","BL","CL","FL","GL","PL")

#com recurso as funcoes ja definidas faz-se a adicao de letras a todos os elementos do tuplo, ou a adicao de todos os elementos de um tuplo ao do outro, de modo a definir as variaveis consoante o pedido

monossilabo_2=("AR","IR","EM","UM") + tuplo_letras(vogal_palavra,"S") + dit_palavra + tuplos(cons_freq,vogal) 

#neste caso, e necessario fazer a funcao tuplos dentro desta mesma para poder juntar primeiro os ultimos dois tuplos, e depois o novo tuplo ao primeiro

monossilabo_3=tuplos(cons,(tuplos(vogal,cons_term))) + tuplos(cons,dit) + tuplos(par_vogal,cons_term)


monossilabo=vogal_palavra + monossilabo_2 + monossilabo_3


silaba_2=par_vogal + tuplos(cons,vogal) + tuplos(vogal,cons_final)


silaba_3=("QUA","QUE","QUI","GUE","GUI") + tuplo_letras(vogal,"NS") + tuplos(cons,par_vogal) + tuplos(cons,tuplos(vogal,cons_final)) + tuplos(par_vogal,cons_final) + tuplos(par_cons,vogal)


silaba_4=tuplo_letras(par_vogal,"NS") + (tuplos(cons,tuplo_letras(vogal,"NS"))) + (tuplos(cons,tuplo_letras(vogal,"IS"))) + tuplos(par_cons,par_vogal) + tuplos(cons,tuplos(par_vogal,cons_final))


silaba_5=((tuplos(par_cons,tuplo_letras(vogal,"NS"))))


silaba_final=monossilabo_2 + monossilabo_3 + silaba_4 + silaba_5


silaba=vogal + silaba_2 + silaba_3 + silaba_4 + silaba_5




def e_monossilabo(monoss):
    """
    funcao que define o monossilabo, verificando todas as regras da gramatica
    
    monoss: string --> palavra a verificar se e monossilabo
    return:booleano --> True no caso de se verificar, False em contrario
    
    """
    if not isinstance(monoss,str):
        raise ValueError ("e_monossilabo:argumento invalido")    
    if monoss in monossilabo:
        return True
    else:
        return False
    
    
    
    
def e_silaba(silab):
    """
    funcao que define a silaba, verificando as regras da gramatica
    
    silab: string --> palavra a ser verificada
    return:booleano --> True no caso de se verificar, False em contrario
    """
    if not isinstance(silab,str):
        raise ValueError("e_silaba:argumento invalido")
    if silab in silaba:
        return True
    else: 
        return False




def e_palavra(x):
    """
    funcao que define a palavra, verificando todos as regras da gramatica
    
    x:string --> palavra a ser verificada
    return:booleano --> True no caso de se verificar, False em contrario
    """
    if not isinstance(x,str):
            raise ValueError("e_palavra:argumento invalido")    
    if palavra_simples(x)=="":
        return True
    elif x in monossilabo:
        return True
    elif x==palavra_simples(x):
        return False
    else:
        return silabas(palavra_simples(x),-5)
#e utilizado o valor -5 para i, uma vez que o tamanho maximo da silaba e 5 carateres



def palavra_simples(x):
    """
    funcao que devolve a palavra sem a silaba final , no caso de a ter,para depois verificar se tudo o resto e silabas
    
    x : string --> palavra a ser verificada
    return: string --> se tiver silaba final, palavra sem esta, se nao tiver , devolve a mesma palavra
    """
    for i in range(5,-1,-1):
        if x[len(x)-i:] in silaba_final:
            return x[:len(x)-i]
        elif x[:i]=="":
            return x




def silabas(x,i) :
    """
    funcao que verifica se a palavra, se as 5 ultimas letras forem silaba, remove-a, se nao ve as ultimas 4
    
    x:string --> palavra sem a silaba final, uma vez que vem da funcao palavra_simples
    i:integer --> numero negativo dos carateres a verificar, uma vez que se verifica os ultimos
    return: string--> volta a fazer a funcao com a palavra sem a silaba encontrada
    return: booleano --> True no caso de ser tudo silaba, ou seja, se a palavra for vazia
    """
    if x=="":
        return True    
    if i==1:
        return False
    if x[i:] in silaba:
            return silabas(x[:i],-5)
    else:
        return silabas(x,i+1)   
