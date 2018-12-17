from balok import balok

pa = int(input('panjang : '))
le = int(input('lebar : '))
ti = int(input('tinggi : '))
semua = balok(pa,le,ti)
ll = semua.luas()
vv = semua.vol()
print(ll,vv)
