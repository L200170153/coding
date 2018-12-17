def cig(a,b):
    if b.lower()=='weekday':
        if 40<=a<=60:
            print('jadi')
        else:
            print('nggak jadi')
    elif b.lower()=='weekend':
        if 40<=a:
            print('jadi')
        else:
            print('nggak jadi')
    else:
        print('not defined')
a = int(input(('how much the cigars : ')))
b = input(('it is on weekday or weekend :'))
cig(a,b)
