def kata(x):
    a = ['satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan']
    b = 'belas'
    c = len(x)
    if int(x)==0:
        print('nol')
    elif int(x)==10:
        print('sepuluh')
    elif int(x)==11:
        print('sebelas')
    elif c == 1:
        print(a[int(x)-1])
    else:
        print(a[int(x[1])-1]+b)
x=''
while x!='exit':
    x = input('angka : ')
    if x=='exit':
        break
    else:
        if int(x) in range(20):
            kata(x)
        else:
            print('angka yang dimasukkan diluar jangkauan / input salah')
