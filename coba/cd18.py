def caught(a,b):
    if b.lower()=='yes':
        if a<=65:
            print('no ticket')
        elif 66<=a<=85:
            print('small ticket')
        else:
            print('big ticket')
    elif b.lower()=='no':
        if a<=60:
            print('no ticket')
        elif 61<=a<=80:
            print('small ticket')
        else:
            print('big ticket')
    else:
        print('invalid input')
a = int(input('your speed : '))
b = input('it is your birthday? (yes/no) : ')
caught(a,b)
