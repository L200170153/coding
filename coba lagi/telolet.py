def tel(x):
    l = []
    for i in range(1,x+1):
        if i%2==0 and i%3==0:
            l.append('om telolet om')
        elif i%2==0:
            l.append('om')
        elif i%3==0:
            l.append('telolet')
        else:
            l.append(str(i))
    print(', '.join(l))
    return l

x = int(input('angka : '))

tel(x)
