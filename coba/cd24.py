def teen(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    d=0
    for i in l:
        if i==15 or i==16:
            d+=i
        elif 13<=i<=19:
            d+=0
        else:
            d+=i
    print(d)
a = int(input('input :'))
b = int(input('input :'))
c = int(input('input :'))
teen(a,b,c)
