
def fat(x):
    y = 1
    while x > 0:
        y = x* y
        x = x - 1
    return y

def fatRec(x):
    if x == 0:
    	return 1
    elif x > 0:
    	return x*fatRec(x-1)
   	 
def somalista(lista1):
    lista = lista1[:]
    x = 0
    if len (lista) == 0:
    	return 0
    else:
    	x = lista[0]
    	del lista[0]
    	return x + somalista(lista)

def multiplicalista(lista1):
    lista = lista1[:]
    if len (lista) == 0:
    	return 1
    else:
    	x = lista[0]
    	del lista[0]
    	return x * multiplicalista(lista)
   	 
   	 
def concatenalistastring(lista1):
    lista = lista1[:]
    if len (lista) == 1:
    	return lista[0]
    else:
    	x = lista[0]
    	del lista[0]
    	return x + concatenalistastring(lista)

def maiorelementolista(lista1):
    lista = lista1[:]
    if len(lista) == 0:
        return "Lista Vazia"
    elif len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > lista[1]:
            del lista[1]
            return maiorelementolista(lista)
        elif lista[0] == lista[1]:
            del lista[0]
            return maiorelementolista(lista)
        else:
            del lista[0]
            return maiorelementolista(lista)


def menorelementolista(lista1):
    lista = lista1[:]
    if len(lista) == 0:
        return "Lista Vazia"
    elif len(lista) == 1:
        return lista[0]
    else:
        if lista[0] < lista[1]:
            del lista[1]
            return menorelementolista(lista)
        elif lista[0] == lista[1]:
            del lista[0]
            return menorelementolista(lista)
        else:
            del lista[0]
            return menorelementolista(lista)

def listapares(lista):
    if len(lista) == 0:
        return []
    else:
        a = lista[0]
        del lista[0]
        if a % 2 == 0:           
            return [a] + listapares(lista)
        else:
            return listapares(lista)
        
    
