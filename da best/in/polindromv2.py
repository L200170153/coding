l = [x for x in input().split(' ')]
m = ''.join(l)
n = m[0:][::-1]
if m==n:
    print('polindrome')
else:
    print('not a polindrome')
    
