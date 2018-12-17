x = int(input('Masukkan angka : '))
l = []
for i in range(1,x+1):
    if i%3==0 and i%5==0:
        l.append(str(i))
print(', '.join(l))
