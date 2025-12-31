#Algortimo de Busca Linear

def buscaLinear(vetor, alvo): 
    
    for i, item in enumerate(vetor):
        if alvo == item: #se o alvo for igual a algum elemento, entao retornamos o indice 
            return i 
        
    return None #senao retornamos None