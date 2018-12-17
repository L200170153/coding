print('program konversi suhu')
suhu = '''
Pilih yang ingin dikonversi
1. Reamur
2. Celcius
3. Fahrenheit
4. Kelvin
'''

a=''
def konversi(a):
    print(suhu)
    a=input('Pilihan anda :')
    while a!='exit':
        if a=='1':
            print('Anda memilih Reamur')
            a=input('exit or lanjut[L] ?')
            if a.lower()=='exit':
                print('terima kasih')
            elif a.lower()=='l':
                konversi2(a)
        elif a=='2':
            print('Anda memilih Celcius')
        elif a=='3':
            print('Anda memilih Fahrenheit')
        elif a=='4':
            print('Anda memilih Kelvin')
    print('terima kasih')
    exit
def konversi2(a):
    print(suhu)
    a=input('Pilihan anda :')
    while a!='exit':
        if a=='1':
            print('Anda memilih Reamur')
            a=input('exit or lanjut[L] ?')
            if a.lower()=='exit':
                print('terima kasih')
            elif a.lower()=='l':
                konversi(a)
        elif a=='2':
            print('Anda memilih Celcius')
        elif a=='3':
            print('Anda memilih Fahrenheit')
        elif a=='4':
            print('Anda memilih Kelvin')
    print('terima kasih')
    exit
konversi(a)

    
