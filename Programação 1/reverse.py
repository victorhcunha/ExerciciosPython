#Reverse
ListaQualquer = [1,2,3,4,5,6,7,8,9]
print(ListaQualquer)
contador = 0
outrocontador = len(ListaQualquer)//2
while outrocontador != 0:
    f = ListaQualquer[contador]
    ListaQualquer[contador] = ListaQualquer[len(ListaQualquer)- 1 - contador]
    ListaQualquer[len(ListaQualquer)- 1 - contador] = f
    contador = contador + 1
    outrocontador = outrocontador - 1
print(ListaQualquer)


    
    
