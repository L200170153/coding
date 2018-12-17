def alarm(a,b):
    if b.lower()=='yes':
        if a in range(1,6):
            print('10:00')
        elif a==0 or a==6:
            print('alarm is off')
        else:
            print('invalid input')
    elif b.lower()=='no':
        if a in range(1,6):
            print('7:00')
        elif a==0 or a==6:
            print('10:00')
        else:
            print('invalid input')
    else:
        print('invalid input!')
a = int(input('day : '))
b = input('it is now vacation? yes/no : ')
alarm(a,b)
