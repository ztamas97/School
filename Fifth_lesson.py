# Gyakorlás

#1. feladat
#Labirintus feladat
#Egy tömb változóba építsünk fel egy pályát, ahol a robotunknak utasítások szerint mozognia kell. A navigálásra a WASD billenytűket
# használjuk. W - előre, S - hátra, A - balra , D - jobbra
# A kiindulási pont ott van ahol az X helyeszkedik el, a cél a C betűnél. A csillag karakterek a fal, arra nem léphetünk rá.
#E billenytű lenyomásánál lépjen ki a program
labirintus = [['*','*','*','*','*','*'],
            ['*','C',' ',' ',' ','*'],
            ['*','*','*','*',' ','*'],
            ['*',' ',' ',' ',' ','*'],
            ['*',' ','*','*','*','*'],
            ['*',' ','*','*','*','*'],
            ['*','X','*','*','*','*'],
            ['*','*','*','*','*','*']]
act = [6,1]
h = [6,1]
play = True
for i in range(0,8):
    for j in range(0,6):
        print(labirintus[i][j],end='')
    print()
while(play):
    go=input('Merre tovább: ')
    if(go == 'E'):
        play=False
    elif(go == 'W'):
        newx = act[0]-1
        newy = act[1]
        if(labirintus[newx][newy] == '*'):
            print('Ez itt fal!')
        else:
            act[0] = newx
            act[1] = newy
    elif(go == 'A'):
        newx = act[0]
        newy = act[1]-1
        if(labirintus[newx][newy] == '*'):
            print('Ez itt fal!')
        else:
            act[0] = newx
            act[1] = newy
    elif(go == 'S'):
        newx = act[0]+1
        newy = act[1]
        if(labirintus[newx][newy] == '*'):
            print('Ez itt fal!')
        else:
            act[0] = newx
            act[1] = newy
    elif(go == 'D'):
        newx = act[0]
        newy = act[1]+1
        if(labirintus[newx][newy] == '*'):
            print('Ez itt fal!')
        else:
            act[0] = newx
            act[1] = newy

    labirintus[h[0]][h[1]]=' '
    labirintus[act[0]][act[1]]='X'
    h[0]=act[0]
    h[1]=act[1]
    for i in range(0,8):
        for j in range(0,6):
            print(labirintus[i][j],end='')
        print()
print('Kilépés...')

#2. feladat Próbáljunk egyszerűsíteni