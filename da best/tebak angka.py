import random 
print('Tebak angka 1-100 !')
a = []
for i in range(101):
    a.append(i)
b = input('ready? jika tidak ketik exit : ')
random.shuffle(a)
coba=0
while b != 'exit':
    print()
    b = input('tebak : ')
    if b == 'exit':
        print()
        print('thx !')
        break
    elif int(b) in a:
        if int(b)==a[0]:
            print('SELAMAT, TEBAKAN ANDA BENAR!')
            break
        elif int(b)>a[0]:
            print('angka yang anda masukkan terlalu besar!')
            coba+=1
            print()
        else:
            print('angka yang anda masukkan terlalu kecil')
            coba+=1
            print()
    else:
        print('invalid input')
        print()
print()
print('ooba :', coba)
