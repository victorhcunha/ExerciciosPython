def find(lista,elemento):
    return find1(lista,elemento,0)
def find1(lista,elemento,n):
    if n == len(lista):
        return False
    elif lista[n] == elemento:
        return True
    else:
        return find1(lista,elemento,n+1)


#Não_Confirmado
def push_stack(lista,elemento):
    lista.append(elemento)
    return lista
def pop_stack (lista):
    del lista[len(lista)-1]
    return lista
def peek_stack(lista):
    return lista[len(lista) - 1]
def push_queue(lista,elemento):
    lista.append(elemento)
def pop_queue(lista):
    del lista[0]
    return lista
