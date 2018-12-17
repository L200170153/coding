import random
a = input('Ready?')
print('GO!')
win=0
lose=0
draw=0
bgk = ['rock','scissors','paper']
while a!='exit':
    print('rock / scissors / paper!')
    a = input('>>> ')
    a = a.lower()
    if a=='exit':
        print()
        print('thx !')
        print('Bye !')
        print()
        break
    elif a=='rock' or a=='paper' or a=='scissors':
        random.shuffle(bgk)
        print('COM :', bgk[0])
        if bgk[0]=='rock':
            if a=='rock':
                print('DRAW!')
                print()
                draw+=1
            elif a=='paper':
                print('player win!')
                print()
                win+=1
            elif tangan=='scissors':
                print('com win!')
                print()
                lose+=1
        elif bgk[0]=='scissors':
            if a=='rock':
                print('player win!')
                print()
                win+=1
            elif a=='paper':
                print('com win!')
                print()
                lose+=1
            elif a=='scissors':
                print('DRAW!')
                print()
                draw+=1
        elif bgk[0]=='paper':
            if a=='scissors':
                print('player win!')
                print()
                win+=1
            elif a=='rock':
                print('com win!')
                print()
                lose+=1
            elif a=='paper':
                print('DRAW!')
                print()
                draw+=1
    else:
        print('Invalid input!')
        print()
print('Win :', win)
print('Lose :', lose)
print('Draw :', draw)
print('Win rate :', ((win+0.5*draw)/(win+lose+draw))*100)
z=input('exit : ')
        
