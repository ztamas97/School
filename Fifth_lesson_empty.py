l = [['*','*','*','*','*','*'],
            ['*','C',' ',' ',' ','*'],
            ['*','*','*','*',' ','*'],
            ['*',' ',' ',' ',' ','*'],
            ['*',' ','*','*','*','*'],
            ['*',' ','*','*','*','*'],
            ['*','X','*','*','*','*'],
            ['*','*','*','*','*','*']]

def kiir():
    for i in range(0,8):
        for j in range(0,6):
            print(l[i][j], end=' ')
        print()
akt=[6,1]
h=[6,1]
kiir()
vege=True
while(vege):
    go=input('Merre: ')
    if(go == 'E'):
        vege=False
    elif(go == 'W'):
        newx=akt[0]-1
        newy=akt[1]
        if(l[newx][newy]=='*'):
            print('Ez fal!')
        else:
            akt[0]=newx
            akt[1]=newy

    elif(go == 'A'):
        newx=akt[0]
        newy=akt[1]-1
        if(l[newx][newy]=='*'):
            print('Ez fal!')
        else:
            akt[0]=newx
            akt[1]=newy

    elif(go == 'S'):
        newx=akt[0]+1
        newy=akt[1]
        if(l[newx][newy]=='*'):
            print('Ez fal!')
        else:
            akt[0]=newx
            akt[1]=newy

    elif(go == 'D'):
        newx=akt[0]
        newy=akt[1]+1
        if(l[newx][newy]=='*'):
            print('Ez fal!')
        else:
            akt[0]=newx
            akt[1]=newy
    l[h[0]][h[1]]=' '
    l[akt[0]][akt[1]]='X'
    h[0]=akt[0]
    h[1]=akt[1]
    kiir()