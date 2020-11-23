rsz_ok = True
while(rsz_ok):
    rsz=input('Kérem a rendszámot "AAA-123" formátumban: ')
    if (rsz != 'VÉGE'):
        if (len(rsz)==7):
            if(rsz[3]=='-'):
                print ('Megfelelő rendszám!', rsz)
                if(rsz[0]=='U' or rsz[0]=='u'):
                    print ('\tÉrvényes motorkerékpár rendszám!')
                else:
                    print ('\tAutó Rendszám!')
            else:
                print ('Hiányzó kötőjel!')
        else:
            print ('Hibás hossz! (',len(rsz),'karater)')
    else:
        rsz_ok = False
print ('Bekérés véget ért!')