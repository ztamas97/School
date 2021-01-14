# Hatodik óra 2020.12.08.

# Mátrixok: Több dimenziós összetett adatszerkezet, amelyben szabadon tárolhatunk több típusú értéket is Pythonban! Más nyelveken ez nem valósul meg.

#1. feladat Készítsünk egy 2×2-es tömböt, majd töltsük fel adatokkal, és kérjük le típusát.
print('1. feladat')
array=[[0,0],
       [0,0],
       [0,0]]
print(type(array))
# Gyakorlatilag egy listát fogok kapni, tehát egy listákat tartalmazó listáról van szó gyakorlatban, melyre minden korábban tanult művelet érvényes.
# írhattuk volna a következő képpen is: array=[[0,0],[0,0]].

# 2. feladat Töltsük fel a a korábban definiált tömböt intekkel STI-ről, majd írassuk ki STO-ra
print('\n2. feladat')
for i in range(len(array)):
    for j in range(len(array[0])):
        array[i][j]= int(input('Érték: '))

print(array)

# 3. feladat A korábban használt mátrixunkhoz adjunk hozzá egy sort. A plusz sor kerüljön előre beállításra. Kódba égetéssel. Majd írassuk ki.
print('\n3. feladat')
newL = [1,1]# camelCase
array.append(newL)
print (array)

# 4. írassuk ki szebben.
print('\n4. feladat')
for i in range(len(array)):
    for j in range(len(array[0])):
        print(array[i][j], end=' ')
    print()

# 5. feladat készítsünk egy tetszőleges hosszúságú listát számokkal, majd rendezzük növekvő sorrendbe.
print('\n5. feladat')
numbers=[5,3,100,1,3]
numbers.sort()
print (numbers)

# 6. feladat készítsünk egy tetszőleges hosszúságú listát számokkal, majd rendezzük csökkenő sorrendbe.
print('\n5. feladat')
numbers=[5,3,100,1,3]
numbers.sort(reverse=True)
print (numbers)

# 6. feladat készítsünk egy tetszőleges hosszúságú listát nevekkel, majd rendezzük növekvő sorrendbe.
print('\n6. feladat')
n=['Anna','Géza','Bogi','Zsolt','Péter']
n.sort()
print (n)