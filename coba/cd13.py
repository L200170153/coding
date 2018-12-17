def akhir(a):
    b=a[-1]
    c=[]
    for i in range(0,len(a)):
        c.append(b)
    print(','.join(c))
a = [x for x in input().split(',')]
akhir(a)
