import random
print('dice rolling...')
true=0
false=0
a = ''
b = [1,2,3,4,5,6]
a = input('ready? input exit for exit : ')
while a!='exit':
    random.shuffle(b)
    a = input('guess the number of dice : ')
    if a=='exit':
        print()
        print('thx !')
        break
    elif int(a)==1 or int(a)==2 or int(a)==3 or int(a)==4 or int(a)==5 or int(a)==6:
        if int(a)==b[0]:
            print('CONGRATULATION!')
            true+=1
            print()
        else:
            print('WRONG!!!')
            false+=1
            print()
    else:
        print('invalid input!')
        print()
print()
print('True :', true)
print('False :', false)
print('Persentage :', str((true/(true+false))*100)+'%')
