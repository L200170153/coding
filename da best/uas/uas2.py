def cek(l):
    b = len(l)//2
    e = 0
    f = 0
    if len(l)%2==0:
        c = l[0:b]
        d = l[b:]
        for i in c:
            e+=int(i)
        for l in d:
            f+=int(l)
    else:
        c = l[0:b+1]
        d = l[b+1:]
        for i in c:
            e+=int(i)
        for l in d:
            f+=int(l)
    if e==f:
        print('True')
    else:
        print('False')
l = ['']
while l[0]!='exit':
    l = [x for x in input().split(',')]
    if l[0].lower() =='exit':
        break
    else:
        cek(l)

print('terimakasih')
    
