#Calcular raiz cúbica
# n = Resultado Positivo e n2 = Resultado Negativo

print ("Cálculo da raiz cúbica")
N = int(input("Digite um número: "))
n = 1
n2 = -1

nnn = n*n*n

while (n*n*n) != N and (n2*n2*n2) != N:
    n = n + 1
    n2 = n2 - 1
    nnn = n*n*n
    nnn2 = n2*n2*n2
    if (nnn > N or nnn == N) and (nnn2 < N or nnn2 == N):
        break
    
if (n*n*n) == N:
    print (n)
elif (n2*n2*n2) == N:
    print (n2)
else:
    print ("Não há resultado inteiro")
