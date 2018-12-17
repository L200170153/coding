import random
a=''
true=0
false=0

b = ['+','x','-',':']
while a.lower()!='exit':
    a = input('Siap?')
    random.shuffle(b)
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    if a.lower()=='exit':
        print('Q.E.D')
        break
    else:
        if b[0]=='+':
            print(number1, b[0], number2, '= ...')
            c = number1+number2
            a = input('Answer = ')
            if int(a)==c:
                print('True !')
                print()
                true+=1
            else:
                print('wrong ! the answer should : ', c)
                print()
                false+=1
        elif b[0]=='-':
            print(number1, b[0], number2, '= ...')
            c = number1-number2
            a = input('answer = ')
            if int(a)==c:
                print('true !')
                print()
                true+=1
            else:
                print('wrong ! the answer should : ', c)
                print()
                false+=1
        elif b[0]=='x':
            print(number1, b[0], number2, '= ...')
            c = number1*number2
            a = input('answer = ')
            if int(a)==c:
                print('true !')
                print()
                true+=1
            else:
                print('wrong ! the answer should : ', c)
                print()
                false+=1
        elif b[0]==':':
            print(angka1, b[0], angka2, '= ...')
            c = angka1//angka2
            print('DIBULATKAN KEBAWAH !')
            a = input('jawaban = ')
            if int(a)==c:
                print('BENAR !')
                print()
                benar+=1
            else:
                print('SALAH ! Jawaban yang benar adalah', c)
                print()
                salah+=1
print()
print('Benar =', benar)
print('Salah =', salah)
print('Nilai =', (benar/(benar+salah))*100)
print()
print('Terima kasih telah mencoba')
                
        
