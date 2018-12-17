from math import sqrt
#q = sqrt((2*c*d)/h)

l=[]
for i in range(1,4):
    a = int(input('masukkan angka : '))
    l.append(str(a))
    
print (', '.join(l))

m=[]
for i in l:
    q = int(sqrt((2*50*int(i))/30))
    m.append(str(q))

print (', '.join(m))

#caralain
print
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(sqrt(2*c*float(d)/h)))))

print (','.join(value))
