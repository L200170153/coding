def kata(num,join=True):
    satuan=['','satu','dua','tiga','empat','lima','enam','tujuh','delapan',
            'sembilan','sepuluh']
    belas=['','sebelas','duabelas','tigabelas','empatbelas','limabelas','enambelas',
           'tujuhbelas','delapanbelas','sembilanbelas']
    puluh=['','sepuluh','duapuluh','tigapuluh','empatpuluh','limapuluh','enampuluh','tujuhpuluh','delapanpuluh','sembilanpuluh']
    kataa = []
    if num==0:
        kataa.append('nol')
    else:
        numstr = '%d'%num
        numstrlen = len(numstr)
        kk = (numstrlen+2)/3
        numstr = numstr.zfill(kk*3)
        for i in range(0,kk*3,3):
            a,b = int(numstr[i+1]),int(numstr[i+2])
            w = kk - (i/3+1)
            if a>1:
                kataa.append(puluh[a])
                if b>=1:
                    kataa.append(satuan[b])
            elif a==1:
                if b>=1:
                    kataa.append(belas[b])
                else:
                    kataa.append(puluh[a])
            else:
                if b>=1:
                    kataa.append(satuan[b])
    if join:
        return ' '.join(kataa)
    return kataa
num=''
while num!='exit':
    num = input('angka : ')
    print kata(num)
