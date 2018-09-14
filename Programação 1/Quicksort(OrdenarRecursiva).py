def quicksort(lista):
    if len(lista) == 0:
        return []
    else:
        pivo = lista[0]
        lista.remove(pivo)
        return quicksort([i for i in lista if i <= pivo]) + [pivo] + quicksort([i for i in lista if i >= pivo])
    
    
