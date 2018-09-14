#Index(indice do item)
ListaQualquer = [1,2,3,4,5,6,7,8,9]
item = 6
contador = -1
for i in ListaQualquer:
    contador = contador + 1
    if i == item:
        break
    
print(contador)
