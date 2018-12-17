a=''
saldo=0
while a.lower()!='exit':
    a = input('input deposit or withdrawal (D/W) : ')
    if a.lower()=='exit':
        break
    else:
        if a[0].lower()=='d':
            b=int(a[2:])
            saldo+=b
        elif a[0].lower()=='w':
            b=int(a[2:])
            if b>saldo:
                print('saldo anda tidak cukup, saldo anda sekarang hanya', saldo)
            else:
                saldo-=b
        elif a.lower()=='cek':
            print(saldo)
        else:
            print('invalid input')

