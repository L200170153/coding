def lucksum(a,b,c):
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    d=0
    for i in l:
        if i!=13:
            d+=i
        else:
            break
    print(d)
a = int(input('input :'))
b = int(input('input :'))
c = int(input('input :'))
lucksum(a,b,c)
