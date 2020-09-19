# Második óra 2020.09.22.

# String
#A string adattípus szöveges értékek tárolására szolgál.
#Pythonban a string frogalma: Unicode karakterek nem módosítható sorozata.

# 1a Tároljanak el egy fruit nevű változóban egy tetszőleges gyümölcs nevét, majd írassák ki képernyőre.
fruit = 'alma' # a stringállandót határolhatjuk ''-vel
fruit = "alma" # de ugyan így működik ""-vel is

print (fruit)
print (type(fruit)) # a típus lekérése a type() függvénnyel történik meg

# 1b Írassa ki képernyőre a drink változóban tárolt string érték 2. karakterét.
drink = 'ásványvíz'
print (drink[1])
# string karakterének kinyerése úgy történik, hogy vesszük a string változót és a neve után helyezett
# []-be írjuk azt, hogy hányadik karaktert szeretnénk kinerni. !FONTOS! az indexelés 0-tól indul!

# 1c Írjuk ki a képernyőre az előző feladatban használt string változóban talált érték 4. karakterének típusát.
print(type(drink[3]))

# 1d Állapítsuk meg hány karakter hosszú egy a felhasználótól bekért string.
s = input('Kérem a nevét: ')
length = len(s)
print (length)

# 1e Az előbb bekért string-nek írjuk a len() függvényel meghatározott értékét.
#print(s[length])
# ebben az esetben hibát fogunk kapni. Ennek oka, hogy a len() a teljes hosszt adja meg, és az indexelés viszont 0-tól indul.
# a túlindexelés hibát kapjuk meg. Az indexelés ebben az esetben egy olyan karakterre mutat ami nem létezik, ezért kapunk hibát.

# 1f Módosítsuk a animal változóba tárolt string harmadik karakterét.
animal = 'Oroszlán'
#animal[2] = 'x'
# Ismét hibát kapunk. A string fogalma tartalmazza, hogy Unicode karakterek nem módosítható sorozata.

# 1g Adott kettő string változó, füzzük őket össze egy s nevű változóba, és írassuk ki Összefűzve: <összefűzött str> formátumban.
s1 = 'Paradicsom'
s2 = 'leves'
s = s1+s2
print ('Összefűzve: ',s)
# Összefűzésre használható a + operátor, melynek két operandusa az összefűzendő tagok.

# 1h Távolítsa el a computer változóban tárolt érték előtt és utánna lévő fehér karatreket(tabulátor, sortörés, szóköz)
computer = '\t Asus \n'.strip()
print (computer)

# A white spacek eltávolítására használható a strip() függvény, ha a paraméter listájátt üresen hagyjuk.

# 1i Távolítsa el a megadott karaktereket a string elejéről, végéről.
computer = '----Dell*****'.strip('-*')
print (computer)

# Megadott karakterek eltávolítására a strip() függvény használható, ha a paraméter litájába '', vagy "" jelek közé meghatározzuk
# a karaktereket.

# 1j Kérjen be a STI-ről egy nevet ezt tárolja egy name nevű változóban, majd kérjen be egy s_name változóba egy keresendő
# keresztnevet. Ellenőrizze hogy a s_name-be tárolt név része e a name változóban tárolt értéknek.
name = input('Kérek egy teljes nevet "Vezetéknév Keresztnév" formátumban: ')
s_name = input('Kérem a keresendő keresztnevet: ')
b = s_name in name
print (b)

# A bekérés a szokott módon az input() függvénnyel történik. A tartalamzás vizsgálatra pedig az in - t használjuk. Az in az
# előtte megadott értéket keresi az utána megadott stringben. Abban az esetben ha megtalálhatő benne True(Igaz) értéket ad vissza
# különben False eredményt kapunk.

# Logikai értékek
# A logikai értékeket a True valamint a False jelöli. FONTOS! A nagy betűs írás ebben az esetben szükséges.
# 2a Hozzunk létre egy bool_t nevű logikai változót, majd állítsuk igazra, írassuk ki a tartalmát.
print('2a')
bool_t = True
print (bool_t)

# 2b Hajtsunk végre két logikai érték(True, False) között az összes lehetséges ÉS műveletet.
print('2b')
print (True and True)
print (True and False)
print (False and True)
print (False and False)

# 2c Hajtsunk végre két logikai érték(True, False) között az összes lehetséges VAGY műveletet.
print('2c')
print (True or True)
print (True or False)
print (False or True)
print (False or False)

# 2d Tároljuk el egy t nevű változóban egy igaz értéket. Majd tagadjuk, és írjuk ki az eredményét.
print('2d')
t = True
print(not t)

# A tagadásra a not operátor, ez egy egy operandosú operátor, hiszen egy értéket tud tagadni.

# 2e Kérjük be egy rendszámot (AAA-111) formátumban. Majd kérjünk be ismét egy rendszámot.
#Ellenőrizzük, hogy megegyezik e a kettő.
nump1 = input('Kérek egy rendszámot (AAA-111): ')
check = input('Kérem a rendszámot ellenőrzéshez: ')
print(nump1==check)

# Az egyenlősáég vizsgálat ra a == tudjuk használni, egyenlőség esetén True értékkel tér vissza, különben False-al
# Másik lehetőség, hogy azt vizsgáljuk két változó nem egyezik e meg, ezt a !=-vel tudjuk megtenni.

# 2f Kérjen be x1 és x2 változóba két számot, majd ellenőrizze a következő relációs műveletekkel a viszonyaikat (<,>,>=,<=)
x1 = int(input('x1: '))
x2 = int(input('x2: '))

print(x1 < x2)
print(x1 > x2)
print(x1 >= x2)
print(x1 <= x2)

# A különböző relációs műveletek eredménye képpen logikai értéket kapok eredményűl a két érték viszonyának megelelőlen.

# Konverzió

# 3a int->float
i = 2
print (float(i))
print (type(float(i)))

# 3b float->int
f = 2.0
print (int(f))
print (type(int(f)))

# 3c int->str
i2 = 2
print(str(i2))
print(type(str(i2)))