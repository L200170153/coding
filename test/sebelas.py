items=[x for x in input().split(',')]
q=[]
for i in items:
    if int(i)%5==0:
        q.append(i)
print (','.join(q),'habis dibagi 5')
    
