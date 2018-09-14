#Remover maior de sublista

def removemaiorsublista(lista):
    g = len(lista) - 1
    while g != -1:
        maior = lista[g][0]
        for i in lista[g]:
            if i > maior:
                maior = i
        lista[g].remove(maior)
        g = g - 1
        
    return (lista)
