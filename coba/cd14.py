def sum2(a):
    b=0
    for i in a[0:2]:
        b+=int(i)
    print(b)
a = [x for x in input().split(',')]
sum2(a)
