#Sort(lista de forma decrescente)
ListaQualquer = [1,2,3,4,5,6,7]
print(ListaQualquer)
contador = 0
contador2 = 0

while contador2 < len(ListaQualquer) - 1:
    contador2 = contador2 + 1
    contador = 0
    while contador < len(ListaQualquer) - 1:
        if ListaQualquer[contador] < ListaQualquer[contador+1]:
            f = ListaQualquer[contador]
            ListaQualquer[contador] = ListaQualquer[contador+1]
            ListaQualquer[contador+1] = f
        contador = contador + 1
   

print(ListaQualquer)
