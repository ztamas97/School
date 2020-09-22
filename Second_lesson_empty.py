# Második óra 2020.09.22.

# String
#A string adattípus szöveges értékek tárolására szolgál.
#Pythonban a string frogalma: Unicode karakterek nem módosítható sorozata.

# 1a Tároljanak el egy fruit nevű változóban egy tetszőleges gyümölcs nevét, majd írassák ki képernyőre.
fruit = 'alma'
print (fruit)

# 1b Írassa ki képernyőre a drink változóban tárolt string érték 2. karakterét.
drink = 'ásványvíz'
print (drink[1])

# 1c Írjuk ki a képernyőre az előző feladatban használt string változóban talált érték 4. karakterének típusát.
print (type(drink[3]))

# 1d Állapítsuk meg hány karakter hosszú egy a felhasználótól bekért string.
str = input('Kérem a nevét: ')
length = len(str)
print(length)

# 1f Módosítsuk a animal változóba tárolt string harmadik karakterét.
animal = 'Oroszlán'
#animal[2] = 't'

# 1g Adott kettő string változó, füzzük őket össze egy s nevű változóba, és írassuk ki Összefűzve: <összefűzött str> formátumban.
s1 = 'Paradicsom'
s2 = 'leves'
s = s1+s2
print('Összefűzve: ',s)

# 1h Távolítsa el a computer változóban tárolt érték előtt és utánna lévő fehér karatreket(tabulátor, sortörés, szóköz)
computer = '\t Asus \n'.strip()
print (computer)

# 1i Távolítsa el a megadott karaktereket a string elejéről, végéről.
computer = '----Dell*****'.strip('-*')
print (computer)

# 1j Kérjen be a STI-ről egy nevet ezt tárolja egy name nevű változóban, majd kérjen be egy s_name változóba egy keresendő
# keresztnevet. Ellenőrizze hogy a s_name-be tárolt név része e a name változóban tárolt értéknek.
name = input('Kérem a teljes nevét: ')
s_name = input('Kérek egy keresztnevet: ')
print(s_name in name)

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

# 2e Kérjük be egy rendszámot (AAA-111) formátumban. Majd kérjünk be ismét egy rendszámot.
#Ellenőrizzük, hogy megegyezik e a kettő.
r1 = input('Kérek egy rendszámot(AAA-111): ')
r2 = input('Kérem az ellenörző rsz.:')
print (r1 == r2)

# 2f Kérjen be x1 és x2 változóba két számot, majd ellenőrizze a következő relációs műveletekkel a viszonyaikat (<,>,>=,<=)
x1 = int(input('x1: '))
x2 = int(input('x2: '))

print(x1<x2)
print(x1>x2)
print(x1<=x2)
print(x1>=x2)

# Konverzió

# 3a int->float
i = 2
print(float(i))

# 3b float->int
f = 2.0
print(int(f))

