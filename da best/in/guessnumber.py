import random 
print('guess number in range 1-100 !')
a = []
for i in range(101):
    a.append(i)
b = input('ready? or not? input exit to exit: ')
print()
random.shuffle(a)
coba=0
while b != 'exit':
    b = input('guess : ')
    if b == 'exit':
        print()
        print('thx !')
        break
    elif int(b) in a:
        if int(b)==a[0]:
            print('CONGRATULATION!!')
            break
        elif int(b)>a[0]:
            print('hmm..too high! try again...')
            coba+=1
            print()
        else:
            print('hmm..too low! try again...')
            coba+=1
            print()
    else:
        print('invalid input')
        print()
print()
print('Try :', coba)
