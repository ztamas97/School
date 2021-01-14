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

x=int(input('x= '))
y=int(input('y= '))
print (szum(x,y))

# 1b Kérjünk be egy számot egy változóba, ha páros akkor kettő, ha páratlan akkor egy értéket kérjünk be másik változókba két számot
# és adjuk össze őket. Ha csak egy számot kellet beadnunk akkor 2 legyen az alap értéke a függvényben a második értéknek
print ('\n1b')
def szum(x,y=2):
    return x+y
l= int(input('Döntés: '))
if l%2==0:
    x=int(input('x= '))
    y=int(input('y= '))
    print (szum(x,y))
else:
    x=int(input('x= '))
    print (szum(x))
    
# 1c Definiáljuk a függvény műlödését.
print ('\n1c')
def szum(x,y=2):
    '''Return the sum of x and y, y default value is 2'''
    return x+y
print(szum.__doc__)

# 1d Készítsünk egy fgv-t a másodfokú egyenlet megoldására.
print ('\n1d')
def sq(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        return [x1, x2]
    elif d == 0:
        return [-b / (2 * a)]
    else:
        return []
print(sq(1,3,2))

# 1e Írjunk egy programot amely bekér három számot és egy függvény segítségével eldönti melyik a legnagyobb (ezt az értéket adja vissza a fgv.).
print ('\n1e')

def maximum(x,y,z):
    if x>y and x>z:
        return x
    if y>x and y>z:
        return y
    else:
        return z

print(maximum(1,2,3))

# 1f Kérjünk be egy stringet a felhasználotól és készítsünk egy függvényt amely a betűit kiírja egymás alá a betüket.
print ('\n1f')
def print_out(s):
    for i in s:
        print(i)
print_out('alma')