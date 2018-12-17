def sum(a):
    b = 0
    for i in a:
        b+=int(i)
    print(b)
a = [x for x in input().split(',')]
sum(a)
