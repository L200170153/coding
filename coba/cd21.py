def brick(a,b,c):
    if a+5*b>=c:
        print('bisa')
    else:
        print('nggak')
a = int(input('small bricks :'))
b = int(input('big bricks :'))
c = int(input('goal :'))
brick(a,b,c)
