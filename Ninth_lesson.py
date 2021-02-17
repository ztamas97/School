#9. óra 2021.02.16.

# Csomagok és modulok
# Modul: Python nyelvű fájl. Definíciókat és utasításokat tartalmaz. Ha a modulhoz az xyz.py fájl
# tartozik, akkor a modulra xyz néven lehet hivatkozni. A modulok más Python programokból importálhatók.
# Csomag: Modulok gyűjteménye. Egy csomag alcsomagokat/modulokat is tartalmazhat. A hierarchiát a csomagon belüli könyvtárszerkezet határozza meg.
# A standard csomagok és modulok a standard könyvtárban találhatók, és nem igényelnek telepítést.

# Random
import random as r

# 1 Generáljunk véletlenszerűen egy számot 1 és 100 között, majd írassuk ki.
print('1. feladat')
num= r.randint(1,100)
print(num)

# 2 Generáljunk úgy -100 és 100 között, hogy csak a randint függvény legyen 
print('\n 2. feladat')
from random import randint
num= randint(-100,100)
print(num)

# 3 Sorsoljunk egy adott szekvenciából véletlenszerűen egy elemet.
print('\n 3. feladat')
import random as r
rsz=r.choice(['alma', 'körte', 'szilva'])
print(rsz)

# 4 Készítsünk programot, amely szimulál egy n hosszú pénzfeldobás sorozatot, majd kiírja a fejek és írások darabszámát!
print('\n 4. feladat')
n=15
dob=[]
for i in range(n):
    dob.append(r.choice('FI'))
print(dob)

# 5 Táruljunk el egy adott időpontot perc pontosággal.
print('\n 5. feladat')
import datetime
t = datetime.datetime(2021, 2, 16, 8, 00, 00)
print(t)

# 6 Nap pontosságban adjunk egy dátumot
print('\n 6. feladat')
d = datetime.date(2020, 2, 16)
print(d)

# 7 Határozzuk meg, hány napja,órája perce, másodperce volt az utolsó óra vége, majd írassuk ki a képernyőre.
print('\n 7. feladat')

t1 = datetime.datetime(2021, 2, 2, 8, 45, 0)
t2 = datetime.datetime(2021, 2, 16, 8, 0, 0)
dt = t2 - t1
print(dt)

# 8 Telepítsük a NumPy könyvtárat
# Tools->Open system shell-> pip3 install numpy
print('\n 8. feladat')

# 9 Hozzunk létre egy numpy tömböt, majd írassuk ki tartalmát.
print('\n 9. feladat')
import numpy as np
npt=np.array([1,2,3])
print(npt)

# 10 Határozzuk meg a dimenziókat, valamint az elemtípust
print('\n 10. feladat')
print(npt.ndim)
print(npt.shape)
print(npt.dtype)