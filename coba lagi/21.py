from math import sqrt
arah=['','']
posisi = [0,0]
while arah[0].lower()!='exit':
    arah = [x for x in input().split(' ')]
    if arah[0].lower()=='up':
        posisi[1]+=int(arah[1])
    elif arah[0].lower()=='right':
        posisi[0]+=int(arah[1])
    elif arah[0].lower()=='down':
        posisi[1]-=int(arah[1])
    elif arah[0].lower()=='left':
        posisi[0]-=int(arah[1])
    elif arah[0].lower()=='cek':
        print('posisi saat ini :', posisi)
    elif arah[0].lower()=='exit':
        break
    else:
        print('invalid input')
print('posisi terakhir :', posisi)
print('jarak :', sqrt(posisi[0]**2 + posisi[1]**2))
print('thanks')

