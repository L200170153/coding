def gjgn(l):
    a = 0
    b = 0
    for i in l:
        if int(i)%2==0:
            a+=int(i)
        else:
            b+=int(i)
    print(a,b)
l = [x for x in input().split(',')]
gjgn(l)
