def lsum(a,b,c):
    if a==b==c:
        print('0')
    elif a==b:
        print(c)
    elif a==c:
        print(b)
    elif b==c:
        print(a)
    else:
        print(a+b+c)
a = int(input('input :'))
b = int(input('input :'))
c = int(input('input :'))
lsum(a,b,c)
