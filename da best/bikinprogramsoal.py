import random
satu = '''
Ini soalnya, harus dijawab ya!
A. Benar satu
B. Salah
C. Apa ini benar?
D. Salah kayaknya?
E. Terserah
'''
dua = '''
Ini soalnya, harus dijawab ya!
A. Benar dua
B. Salah
C. Apa ini benar?
D. Salah kayaknya?
E. Terserah
'''
tiga = '''
Ini soalnya, harus dijawab ya!
A. Benar tiga
B. Salah
C. Apa ini benar?
D. Salah kayaknya?
E. Terserah
'''
empat = '''
Ini soalnya, harus dijawab ya!
A. Benar empat
B. Salah
C. Apa ini benar?
D. Salah kayaknya?
E. Terserah
'''
soal = [satu,dua,tiga,empat]
nilai=100
benar=0
salah=0
random.shuffle(soal)

while len(soal)!=0:
    for i in soal:
        print(i)
        jawab=input('Masukkan jawaban anda :')
        if i==satu:
            if jawab.lower()=='a':
                print('jawaban anda benar')
                benar+=1
            else:
                print('jawaban anda salah')
                salah+=1
                nilai-=25
            soal.remove(i)
        elif i==dua:
            if jawab.lower()=='b':
                print('jawaban anda benar')
                benar+=1
            else:
                print('jawaban anda salah')
                salah+=1
                nilai-=25
            soal.remove(i)
        elif i==tiga:
            if jawab.lower()=='c':
                print('jawaban anda benar')
                benar+=1
            else:
                print('jawaban anda salah')
                salah+=1
                nilai-=25
            soal.remove(i)
        elif i==empat:
            if jawab.lower()=='d':
                print('jawaban anda benar')
                benar+=1
            else:
                print('jawaban anda salah')
                salah+=1
                nilai-=25
            soal.remove(i)
print()
print('benar : ',benar)
print('salah :', salah)
print('nilai :', nilai)
