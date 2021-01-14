# Hetedik óra 2021.01.05.

# Függvények
# A függvény névvel ellátott alprogram, amely a program más részeiből meghívható. Függvények
# használatával a számítási feladatok kisebb egységekre oszthatók. A gyakran használt függvények
# kódját könyvtárakba rendezhetjük.

# Egy változónak értékül adhatunk egy függvényt.
# Függvényeket lehet egymásba ágyazni.
# Egy függvény kaphat paraméterként függvényt ill. adhat eredményül függvényt.

# 1a Adjunk össze két számot egy szum függvény segítségével, amely két változót kap, és ezek összegét adja vissza.
print ('1a')
def szum(x,y):
    return x+y

ossz=szum(2,3)
print(ossz)

# 1b Kérjünk be egy számot egy változóba, ha páros akkor kettő, ha páratlan akkor egy értéket kérjünk be másik változókba két számot
# és adjuk össze őket. Ha csak egy számot kellet beadnunk akkor 2 legyen az alap értéke a függvényben a második értéknek.
print ('\n1b')

def szum(x,y=2):
    return x+y

l=int(input('döntés: '))

if l%2==0:
    x=int(input('x= '))
    y=int(input('y='))
    print(szum(x,y))
else:
    x=int(input('x= '))
    print(szum(x))
    
# 1c Definiáljuk a függvény működését.
print ('\n1c')
def szum(x,y=2):
    '''the function return the sum of two digits'''
    return x+y
print(szum.__doc__)

# 1d Készítsünk egy fgv-t a másodfokú egyenlet megoldására.
print ('\n1d')

def sqr_solve(a,b,c):
    d= b**2 - 4 * a * c
    if d>0:
        x1= (-b + d**0.5)/(2*a)
        x2= (-b - d**0.5)/(2*a)
        return [x1,x2]
    elif d == 0:
        return [-b / (2*a)]
    else :
        return []

print(sqr_solve(1,3,2))

# 1e Írjunk egy programot amely bekér három számot és egy függvény segítségével eldönti melyik a legnagyobb (ezt az értéket adja vissza a fgv.).
print ('\n1e')

def maximum(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

print(maximum(1,2,3))

# 1f Kérjünk be egy stringet a felhasználotól és készítsünk egy függvényt amely a betűit kiírja egymás alá.
print ('\n1f')

def print_data(s):
    for i in s:
        print(i)

s = input('szó: ')
print_data(s)