def kuadrat(n,m):
    k = dict()
    for i in range(n,m+1):
        k[i]=i**2
    for a,b in k.items():
        print(a,b)
n = int(input('batas bawah :'))
m = int(input('batas atas :'))
kuadrat(n,m)
