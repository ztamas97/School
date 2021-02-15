# Alap Feladat

print("DOLDOZAT ÉRTÉKELŐ PROGRAM")
pontszam = input ("Kérem a dolgozat pontszámát")

f = int(pontszam)


a = False 
b = False 
c = False 
d = False 
e = False

if (int(pontszam) < 0 ) :
    a = True
if (int(pontszam) > 100 ) :
    b = True

if (int(pontszam) >= 0 ) :
    c = True
if (int(pontszam) <= 100 ) :
    d = True

if a == True or b == True :
    print("Érvénytelen a beadott pontszám!")

if a == True or b == True :
    e = False

if c == True and d== True and e == False :
    print("Megfelelő pontszám!")

# 1. Feladat

tanulo = input("Kérem a tanuló nevét: ")

print("Tanuló: " , tanulo)
print(tanulo , ": " , pontszam," pont")

# 2. Feladat

e = False
g = False
i = False
k = False
m = False


if 50 >= f >= 0 :
    e = True

if 60 >= f >= 51 :
    g = True

if 75 >= f >= 61 :
    i = True

if 90 >= f >= 76 :
    k = True

if 100 >= f >= 91 :
    m = True

if e == True :
    print(tanulo, ": Elégtelen")
    
if g == True :
    print(tanulo, ": Elégséges")

if i == True :
    print(tanulo, ": Közepes")
    
if k == True :
    print(tanulo, ": Jó")
    
if m == True :
    print(tanulo, ": Jeles")


# 3. Feladat

tanulo2 = input("Kérem a tanuló nevét: ")


e2 = False
g2 = False
i2 = False
k2 = False
m2 = False
f2 = 0
if 50 >= f >= 0 :
    e2 = True

if 60 >= f >= 51 :
    g2 = True

if 75 >= f >= 61 :
    i2 = True

if 90 >= f >= 76 :
    k2 = True

if 100 >= f >= 91 :
    m2 = True


if e2 == True :
    f3 = (": Elégtelen")
    
if g2 == True :
    f3 = (": Elégséges")

if i2 == True :
    f3 = (": Közepes")
    
if k2 == True :
    f3 = (": Jó")
    
if m2 == True :
    f3 = (": Jeles")

while f2 <= 51 :
    f2 = int(input("Kérem a dolgozat pontszámát: "))
    if f2 >=51 :
        print( "Pontszám: ", f2, " Pont" "\n", "Tanuló: ", tanulo2,"\n", tanulo2 ,": ", f3, )
    else :
        print( "Pontszám: ", f2, "\n", "Tanuló: ", tanulo2,"\n", tanulo2 ,": ", "Elégtelen, próbálja újra!")