import random
tangan = input('Ready?')
print('GO!')
print()
menang=0
kalah=0
seri=0
bgk = ['batu','gunting','kertas']
while tangan!='exit':
    print('batu / gunting / kertas!')
    tangan = input('>>> ')
    tangan = tangan.lower()
    if tangan=='exit':
        print()
        print('kok udahan!')
        print('Bye!')
        print()
        break
    elif tangan=='batu' or tangan=='kertas' or tangan=='gunting':
        random.shuffle(bgk)
        print('COM :', bgk[0])
        if bgk[0]=='batu':
            if tangan=='batu':
                print('yah seri!')
                print()
                seri+=1
            elif tangan=='kertas':
                print('player menang!')
                print()
                menang+=1
            elif tangan=='gunting':
                print('com menang!')
                print()
                kalah+=1
        elif bgk[0]=='gunting':
            if tangan=='batu':
                print('player menang!')
                print()
                menang+=1
            elif tangan=='kertas':
                print('com menang!')
                print()
                kalah+=1
            elif tangan=='gunting':
                print('yah seri!')
                print()
                seri+=1
        elif bgk[0]=='kertas':
            if tangan=='gunting':
                print('player menang!')
                print()
                menang+=1
            elif tangan=='batu':
                print('com menang!')
                print()
                kalah+=1
            elif tangan=='kertas':
                print('yah seri!')
                print()
                seri+=1
    else:
        print('Invalid input!')
        print()
print('Menang :', menang)
print('Kalah :', kalah)
print('Seri :', seri)
z=input('ketik exit : ')
        
