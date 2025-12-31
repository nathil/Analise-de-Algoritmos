#Algoritmos Iterativo e Recursivo de Busca Binária 

def buscaBinaria_Iter(vetor, alvo): 
    inicio = 0 
    fim = len(vetor) - 1 

    while fim - inicio > 1: #o algoritmo para quando não houver elementos entre eles
        meio = (inicio + fim)//2 #para calcular o meio usamos a media entre os numeros 
        
        if alvo == vetor[meio]: #quando o alvo for igual ao meio então encontramos o valor 
            return meio
        
        elif alvo < vetor[meio]: #se o alvo for menor que o meio alteramos o valor do fim 
            fim = meio 
            
        else: #se o alvo for maior que o meio alteramos o valor do inicio 
            inicio = meio


def buscaBinaria_Recur(vetor, alvo, inicio=None, fim=None): 

    if inicio is None:
        inicio = 0 
    
    if fim is None: 
        fim = len(vetor) - 1 

    meio = (inicio + fim)//2 #para calcular o meio usamos a media entre os numeros 
    
    if alvo == vetor[meio]:
        return meio
    
    elif fim - inicio <= 1: #o algoritmo para quando não houver elementos entre eles
        return None
    
    elif alvo < vetor[meio]: #se o alvo for menor que o meio então chamamos a função alterando o fim pelo meio
        return buscaBinaria_Recur(vetor, alvo, inicio, meio)  
    
    return buscaBinaria_Recur(vetor, alvo, meio, fim) #se o alvo for maior que o meio então chamamos a função alterando o inicio pelo meio
