def kata(num,join=True):
    satuan=['','satu','dua','tiga','empat','lima','enam','tujuh','delapan',
            'sembilan','sepuluh']
    belas=['','sebelas','duabelas','tigabelas','empatbelas','limabelas','enambelas',
           'tujuhbelas','delapanbelas','sembilanbelas']
    kataa = []
    if num==0:
        kataa.append('nol')
    else:
        numstr = '{}'.format(num)
        numstrlen = len(numstr)
        kk = (int(numstr)+2)/3
        numstr = numstr.zfill(kk*3)
    print(kk)
    return kataa
kata(11)
