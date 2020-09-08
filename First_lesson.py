# Első óra 2020.09.08.

# Python nyelven írodott kódok kiterjesztése .py

# Kiíratás
# 1 Kiíratás képernyőre print fügvénnyel.
print('Hello word!')
    
#A ('Hello word!') helyett megfelelő a ("Hello word!") szintaktika is! a Python fordító ezen nem problémázik!
#Bizonyos programozási nyelveknél a '' csak karaktert tartalmazhat, karakter sorozat(pl. string) csak "" között lehet.
#De Pythonnál ezen nem kell problémáznunk. :)
#Viszont a programunk akkor szép, ha szisztematikusan egyik fajta megoldást használjuk.
    

# Alap műveletek
# 2a Adjunk össze két számot (pl. 5+3)
print(5+3)

# 2b Adjuk meg a 1592 és a 124 különbségét
print(1592-124)

# 2c Határosszuk meg 1250 és 123 szorzatát
print(1250*123)

# 2d Tároljuk el 100-et egy x nevű változóba, 23-mat pedig egy y nevű változóba, határozzuk meg x és y változók értékeinek hányadát.
x=100
y=23
# változó definiálásához kell választanunk egy nevet (pl.: x,y), elegánsabb igaz, ha magyarázó neveket adunk (pl.: number1, number2)
# a megadott értéknek nem kell meghatároznunk a típusát. A Python gyengén típusos nyelvek közé tartozik, az előbb említett tulajdonság miatt.
print(x/y) # a / -vel történő osztás eredménye egy float (pl.: 5.0;3.7)
print(x//y) # a // -vel történő osztás eredménye egy integer (pl.: 5;4), használata veszélyes,
            # hiszen kerekítés, vagy bármi nélkül levágja az tört részt (csak az egész részt adja)
print(x%y) # a % -al történő osztás ereménye az osztás maradéka

# 2e Adjuk meg 2 ötödik hatványát
print(2**5)

# String - basics
#3a Tárolja el egy változóba a nevét, majd irassa ki képernyőre!
name = 'Tamás'
print(name)

#3b Tároljunk el egy house változóba egy háztipust (Családiház, Társasház, Panelház), majd egy következő sorba ismét a house változóba egy eltérőt, irassuk ki az eredméynt!
house = 'Családiház'
house = 'Trásasház'
print (house)

# az eredmény a második értékadásnál adott érték lesz, hiszen megváltozott a változó tartalma, kvázi felülírtuk! Erre mindig figyelni kell!

#Bekérés
# 4a Kérjünk be egy name nevű változóba egy nevet, majd írjuk ki a képernyőre egy üdvözlő üzenetet. (pl.: be->Ádám, Hello Ádám!)
name = input('Név: ')
print ('Hello ' + name + '!')
print ('Hello ', name, '!')
# Bekéréshez az input függvényt tudjuk használni. A zárojelek közé, a felhasználónak megjelenített üzenetet tudjuk idézőjelek közé beírni.
# A idézőjel itt lehet '', de lehet "" is. A bekérés eredméynét egy változóba kell eltárolnunk.
# FONTOS! A bekérés eredménye mindig string, ha számot adunk meg akkor is!

# A kiíratásba egy kis csalás van, hiszen több külön álló részt akarunk kiíratni. Összefűzni úgy tudjuk ezeket, hogy a részek közé , -t rakunk
# vagy + jellel össze fűzzük