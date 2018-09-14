#Entre maiores

def entremaiores(lista):

    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    lista2 = lista[:]
    lista2.remove(maior)
    maior2 = lista2[0]
    for f in lista2:
        if f > maior2:
            maior2 = f
    h = lista.index(maior)
    h2 = lista.index(maior2)
    lista3 = []
    if h > h2:
        t = h2
        h2 = h
        h = t
        lista3.append(maior2)
        h3 = h
        while h3 < h2:
            lista3.append(lista[h3+1])
            h3 = h3 + 1 
    else:
        lista3.append(maior)
        h3 = h
        while h3 < h2:
            lista3.append(lista[h3+1])
            h3 = h3 + 1 
    
    return(lista3)
        
        
