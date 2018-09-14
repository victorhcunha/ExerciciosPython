def maximo (lista):
    if lista == []:
        return []
    elif len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > lista[1]:
            del lista[1]
        else:
            del lista[0]
        return maximo(lista)

def ordenar(lista):
    if lista == []:
        return []
    elif len(lista) == 1:
        return lista
    else:
        a = maximo(lista[:])
        lista.remove(a)
        return ordenar(lista) + [a]
