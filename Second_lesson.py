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
animal[2] = 'x'
# Ismét hibát kapunk. A string fogalma tartalmazza, hogy Unicode karakterek nem módosítható sorozata.

# 1g 