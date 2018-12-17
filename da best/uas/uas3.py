def putar(l):
    k = []
    a = l[-2:]
    b = l[0:len(l)-2]
    for i in a:
        k.append(i)
    for l in b:
        k.append(l)
    print(k)
l = [x for x in input().split(',')]
putar(l)
