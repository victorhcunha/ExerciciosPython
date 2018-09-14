def verificarsubstring(lista, dupla):
    h = 0
    lista = list(lista)
    lista2 = []
    while h < len(lista) - 1:
        lista2.append(lista[h] + lista[h+1])
        h = h + 1
    verific = 0
    for i in lista2:
        if dupla == i:
            verific = 1
    if verific == 1:
        lista3 = list(dupla)
        d = lista.index(lista3[0])
        return d
    else:
        return "false"
