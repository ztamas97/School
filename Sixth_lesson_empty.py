# Hatodik óra 2020.12.08.

# Mátrixok: Több dimenziós összetett adatszerkezet, amelyben szabadon tárolhatunk több típusú értéket is Pythonban! Más nyelveken ez nem valósul meg.

#1. feladat Készítsünk egy 2×2-es tömböt, majd töltsük fel adatokkal, és kérjük le típusát.
print('1. feladat')
mtx=[[0,0],
     [0,0]]

print(type(mtx))


# 2. feladat Töltsük fel a a korábban definiált tömböt intekkel STI-ről, majd írassuk ki STO-ra
print('\n2. feladat')
for i in range(len(mtx)):
    for j in range(len(mtx[0])):
        mtx[i][j]=int(input('Érték: '))
print(mtx)

# 3. feladat A korábban használt mátrixunkhoz adjunk hozzá egy sort. A plusz sor kerüljön előre beállításra. Kódba égetéssel. Majd írassuk ki.
print('\n3. feladat')
row = [3,3]
mtx.append(row)
print(mtx)

# 4. írassuk ki szebben.
print('\n4. feladat')
for i in range(len(mtx)):
    for j in range(len(mtx[0])):
        print(mtx[i][j],end=' ')
    print()

# 5. feladat készítsünk egy tetszőleges hosszúságú listát számokkal, majd rendezzük növekvő sorrendbe.
print('\n5. feladat')
l=[6,100,3,1,200,23]
l.sort()
print(l)


# 6. feladat készítsünk egy tetszőleges hosszúságú listát számokkal, majd rendezzük csökkenő sorrendbe.
print('\n5. feladat')
l=[6,100,3,1,200,23]
l.sort(reverse=True)
print(l)

# 6. feladat készítsünk egy tetszőleges hosszúságú listát nevekkel, majd rendezzük növekvő sorrendbe.
print('\n6. feladat')
n=['Béla','Judit','Zsombor','Anna']
n.sort()
print(n)

# 7. feladat most rendezzünk úgy egy listát, hogy a sorrend ne változzon, hanem egy új listába kerüljön bele
print('\n7. feladat')
l=[6,100,3,1,200,23]
l2=sorted(l)
print(l)
print(l2)