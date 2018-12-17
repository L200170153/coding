a=['','']
saldoku=0
while a[0].lower()!='exit':
    a = [q for q in input('Deposito or Withdrawal ?').split(' ')]
    if a[0].lower()=='d':
        saldoku+=int(a[1])
    elif a[0].lower()=='w':
        if int(a[1])<=saldoku:
            saldoku-=int(a[1])
        else:
            print('Maaf, Saldo Anda kurang! Sisa saldo Anda sekarang Rp', saldoku)
    elif a[0].lower()=='cek':
        print('Saldo Anda sekarang Rp', saldoku)
    elif a[0].lower()=='exit':
        break
    else:
        print('Invalid Input! Try Again!')
print('terima kasih')
