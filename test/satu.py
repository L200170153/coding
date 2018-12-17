l=[] #mendefinisikan bahwa l adalah list kosong, nanti akan diisi dengan i
for i in range(2000, 3201): #jaraknya antara 2000-3200, 2000 sebagai awal, 3201 sebagai batas(tidak dihitung)
    if i%7==0 and i%5!=0: #hanya akan terjadi jika memenuhi 2 syarat tsb
        l.append(str(i)) #menjadikan i dalam sebuah list dan membuatnya menjadi string

print ','.join(l) #menjadikan l dalam bentuk string, ',' untuk memisahkan tiap string dengan koma

#exercise
#modifikasi

l=[]
for i in range(10,100):
    if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        l.append(str(i))
print ', '.join(l)
