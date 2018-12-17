d = dict()
m = int(input('masukkan batas bawah : '))
n = int(input('masukkan batas atas : '))
for i in range(m,n+1):
    if i%2==0:
        d[i]='genap'
    else:
        d[i]='ganjil'
for a,b in d.items():
    print(a,b)
