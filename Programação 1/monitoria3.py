# Inteiros entre eles

n = int(input())
m = int(input())

if n < m:
    for i in range(n+1,m):
        print(i)

elif m < n:
    for i in range(m+1,n):
        print(i)

else:
    print ("Iguais")
