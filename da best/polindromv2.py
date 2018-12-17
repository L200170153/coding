l = [x for x in input().split(' ')]
m = ''.join(l)
n = m[0:][::-1]
if m==n:
    print('polindrom')
else:
    print('bukan polindrom')
    
