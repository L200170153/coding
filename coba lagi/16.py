b = []
def ganjil(a):
    for i in a:
        if int(i)%2==1:
            b.append(i)
    print(','.join(b))
a = [x for x in input().split(',')]
ganjil(a)
