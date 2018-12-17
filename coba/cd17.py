def fash(you,date):
    if you<=2 or date<=2:
        print('no')
    elif you>8 or date>8:
        print('yes')
    else:
        print('maybe')
you = int(input('your stylishness : '))
date = int(input('your date stylishness : '))
fash(you,date)
