# Harmadik óra 2020.10.06.

# Vezérlési szerkezetek

# A vezérlési szerkezet segítségével a megírt programunk bonyolultabb feladatok megoldására is képes lesz.
# Vezérlési szerkezetek közé soroljuk a különböző elágazásokat(if, elseif, else), melyekkel döntési szituációkat tudunk létrehozni,
# valamint a különböző ciklusokat(for, while) is.
# Pythonban a vezérlési szerkezetek belsejét indentálással (azaz beljebb írással) kell jelölni. (lásd késöbb)

# IF utasítás
# példa:
# if feltétel1:
#    utasítás1
# else:
#    utasítás2
# Hogyan is működik? A program futás során megvizsgálja, hogy az if(ha) után írt feltétel teljesül-e, ha igen akkor az alatta lévő
# utasítás végre hajtódik, a többi így már nem. Ha nem teljesül a feltétel, akkor az első utasítás nem kerül végrehajtásra,
# hanem a else(különben) után írtakkal fog folytatódni a programunk futása.
# Ha ilyen jellegű elágazást szeretnénk a programunkban akkor mindig minimum egy if utasítást kell tartalmaznia! Az else egy nem
# kötelező elem!

# 1a Egy automatizált kiszolgálási rendszert készítünk. Első lépésben kérdezzük meg a felhasználót, hány éves. Abban az esetben
# ha betöltötte a 18 éves kort, akkor a 'Kaphatsz sört!' szöveget jelenítsük meg, ha nem akkor a 'Nem tudlak kiszolgálni!'
# eredményt irassuk ki.
print('1a : Kiszolgálás')
yo = int(input('Hány éves vagy? '))
if yo >= 18 :
    print('Kaphatsz sört!\n')
else:
    print('Nem tudlak kiszolgálni!\n')
# Az adat bekérés a szokásos módon történik meg, ügyelve arra, hogy számot kérünk be. az if kulcsszó után végzünk egy relációt
# abban az esetben ha ez True, vagyis igaz eredményt ad vissza akkor az alatta lévő utasítást hajtjuk végre, ami most kiíratás.
# Minden más esetben az else ágban lévő utasítást.
# A szövegek végére írt \n egy sortörést rak a sor végére.

# 1b A közlekedési hatóság számára kell egy olyan programot készítenünk, amely meghatározza, hogy adott koru személy számára
# milyen típusú jogosítványok adhatoak ki. A kor bekérésekor figyeljünk arra, hogy engedélyezett a 22.5 beírás pl. tehát nem csak
# egészek adhatóak meg!
# Jogosítvány kategóriák:
# A -> 23.5 év
# AM -> 15.5 év
# B -> 17 év
print('1b : Jogosítvány megszerzése')
yo = float(input('Hány éves vagy? '))
if yo >= 23.5:
    print('AM,B,A\n')
elif yo >= 17:
    print('AM,B\n')
elif yo >= 15.5:
    print('AM\n')
else:
    print('Túl fiatal!\n')

# A bekérésnél ebben az esetben figyelnünk kell, hogy nem int() konverziót, hanem float() konverziót kell használnunk.
# Az ellenörzésnél előszőr a legmagasabb kor követelményt vizsgáljuk, ha azt valaki teljesíti akkor a felsorolt jogosítványokból
# mindent megkaphat, a többi ág nem kerül vizsgálatra. Abban az esetben viszont ha nem teljesül, vizsgáljuk a következő feltételt.
# fontos, hogy több döntési szituációt adhatunk meg, elif(elsif- különben ha) kulcsszóval.
# Tehát egy elégazás tartalmaz minimum 1 if-et, tartalmazhat 0- amennyi szükséges elif-et, és 0, vagy 1 db else-t.

# 1c Egy jelszó ellenörző programot készítünk. A döntésünk alapja, hogy megfelelő e, a jelszó, a hossza.
# Kérjen be a felhasználótól egy 8-16 karakter hosszú jelszót. Következő ellenörzési feltételek valósuljanak meg:
# - 0-7 karakter - Túl rövid! Nem elfogadhtató!
# - 8-10 karakter - Alacsony biztonság!
# - 11-14 karakter - Közepes biztonság!
# - 15-16 karakter - Magas biztonság!
# - 16+ Túl hosszú! Nem elfogadható!
print ('\n1c : Jelszó ellenőrzés')
psw = input('Jelszó: ')
length = len(psw)
if length > 16:
    print('Túl hosszú! Nem elfogadható!')
elif length >= 15:
    print('Magas biztonság!')
elif length >= 11:
    print('Közepes biztonság!')
elif length >=8:
    print('Alacsony biztonság!')
else:
    print('Túl rövid! Nem elfogadhtató!')
print('A jelszava értékelve!\n')

# Abban az esetben, ha az elágazás utolsó eleme után, de kijebb írunk valamit az mindenképpen megtörténik a
# a kiértékeléstől függetlenűl. Ebben az esetben a print('A jelszava értékelve!\n') mindig megtörténik.

# While

# while feltétel:
#     utasítás

# A while egy olyan szerkezet, melyben az adott utasítást addig ismét és ismét megcsináljuk, ameddig a feltétel igaz.
# ha a feltétel ereménye hamis, akkor a whilenak vége.
# Egy jól megírt program esetén az utasítás a feltételt hamisra kell állítsa egy idő után, különben végtelen ciklust kapunk.
# Az utasítást, más néven ciklusmagot mindaddig hajtja végre tehát a program, ameddig nincs változás a feltétel kiértékelsekor.
# Egy lefutását a ciklusmagnak egy iterációnak nevezzük. Akkor hasznos a while használata ha előre nem ismert, mennyi lesz az
# iterációk száma.

# 2a Programozás dolgozatot írunk. Az eredményünk ellenörzésére készítsünk egy programot.
# Kérjünk be egy pontszámot. Abban az esetben ha a pont érték 10 alatt van az 'Érdemjegy: 1' ereményt írassuk ki.
# Természetesen ilyet senki sem szeretne, ezért ismét megírja az adott illető a dolgozatot, és mind addig, amíg minimum határt
# el nem éri. Ha sikeres a dolgozat írjuk ki a képernyőre, a 'Gratulálok, sikeresen megírtad a dolgozatot!' szöveget.
print('2a : Dolgozat ellenőrzés')
while int(input('Pontszám: ')) < 10:
    print('Érdemjegy: 1')
print('Gratulálok, sikeresen megírtad a dolgozatot!')

# A feltételünk ebben az esetben a while után az, hogy hogy a bekért érték, kisebb e mint 10, ha ez True eredmény ad vissza
# akkor a ciklusmag fog lefutni, és újra ellenőrizzük a feltételt. Ha 10, vagy annál nagyobb a bekért érték,  reláció eredménye
# False lesz, ezért a ciklusmag nem fut le újra, hanem a program futása a cikluson kivül tovább folyik.

# 2b Készítsen egy jelszó ellenőrző progrmot, amely mind addig fog bekérni jelszót a felhaszbálótól,
# ameddig az megfelelő nem lesz. Az a jelszó megfelelő, amelyik minimum 10 karakter hosszú, maximum 32.
# Ha nem megfelelő a jelszó erről tájékoztassuk a felhasználót, és ugynúgy az elfogadott jelszó tényéről is.
print('\n2b: Jelszó ellenőrzés')
psw_ok = True
while psw_ok:
    psw = input('Jelszó: ')
    if len(psw) >= 10 and len(psw) <= 32:
        psw_ok = False
    else:
        print ('Nem megfelelő a jelszó hossza! Hossz:', len(psw))
print('Sikeres jelszó megadás! Új jelszó: ', psw)

# A feladatban a feltétel ellenőrzése nem a while után látható, ott csak a kiértékelést tartalmazó változó van.
# Itt mindig minimum 1* lefut a ciklusmag, az előző feladatban nem!
# A feltétel eredményének állítása akkor történik meg egyedül, ha az if True értéket ad vissza, ekkor a psw_ok
# változót False ra állítjuk, és a ciklus véget fog érni.

#2c Készítsünk egy számkitalálós játékot. A programunk véletlenszerűen generáljon egy egész számot 1 és 100 között. Majd kérjen be a
# felhasználótól is egy egészet. Ha megyegyezik a kettő a user nyert, ha nincs egyezés, írjuk ki, hogy a tipp kisebb vagy nagyobb
# mint a kisorsolt szám, és kérjünk be egy új tippet.
print('\n2c: Számkitalálós játék')
import random
num = random.randint(1,100)
print('Puska: ', num)
tipp = 0
while tipp != num:
    tipp = int(input('Tipp:'))
    if(tipp > num):
        print('Túl nagy!')
    elif(tipp < num):
        print('Túl kicsi!')
    else:
        print('Gratulálok, eltaláltad!')
# A random szám generálása később lesz részletesebben is. Egynelőre csak annyi, hogy a program elejére mindig kell egy import random
# A generálás pedig a random.randint(min,max) meghívásával történik meg.
# A feltételünk az, hogy a tipp nem egyenlő a számmal amit generáltunk. Amíg ez igaz mindig kérjünk be egy új számot,
# és ellenőrizzük a generálthoz képest eltér e, ha nem akkor írjuk ki ezt.

# For

# for elem in szekvencia:
#    utasítás

# A for, vagy számlálós ciklus esetében fontos, hogy ismerjük az iterációk számát. A ciklus egy adott szekvencián(sorozaton)
# halad végig, mondjuk egy intervallumon(0-100), egy stringen, egy összetett adatípus elemein(lásd később.).
# Az adott elemmel, pedig végrehajtja a ciklusmagban lévő utasítást. Fontos mindig annyiszor fut le a programunk,
# ahogyan azt definiáltuk.

# Értéktartomány létrehozása. Ez egy fontos lépés, hiszen a ciklus működése során, ha számokkal dolgozunk ebben 'lépkedünk'
print('\nRange működése:')
for i in range(1,10):
    print(i , end=',')
# Az i a változó mely folyamatosan változik, a range az intervallum melyben mozgunk. Az intervallumunk alsó értéke az első szám
# a második szám viszont már olyan, amit nem vehet fel az elem amit változtatunk, esetünkben az i.
# a print függvény egy új lehetőségét is láthatjuk, az end kulcsszóval tudjuk megmondani mi legyen a sor vége elem, ami
# alap esetben egy sortörés(enter)

# 3a Írassuk ki a felhasználó által megadott pozitív egész számig, a számok négyzetét.
print('\n\n3a: négyzetszámok kiíratása')
n = int(input('n: '))
for i in range (1, n+1):
    print(i**2, end=', ')
# A rangenek megadott paraméter lehet változó is mint látjuk. Fontos a felső határt nem érjük el amikor iterálunk végig az
# elemeken, ezért a megadott értékhez hozzá adunk 1-et, és máris feloldottuk a problémát.

# 3b Kérjünk be a felhasználótól egy nevet. Majd írjuk ki, egyesével a betűit egymás alá az adott névnek.
print('\n\n3b: Név betűinek kiíratása')
name= input('Kérem a nevét: ')
for i in range (len(name)):
    print(name[i])
# A stringen történő végig járás, tehát végig iteráláshoz tudnunk kell meddig kell növelni az i értékét. A hossz lekérdezéséhez
# a len függvényt használtuk. Ez megadta milyen hosszú a beadott érték. Egyedűl ezt az értéket adtuk át a rangenek.
# Ha csak egy paramétere van a rangenek, az azt jelenti, hogy 0-tól indul, 1-el kisebb értékig mint a megadott.
# Ez nekünk pont praktikus, hiszen a stringet 0-tól indexeljük.(Lásd Second_lesson.py)

# 3c n-szer n-es hárömszög kiíratása * karakterekből
# Példa:
# n: 4
# *
# * *
# * * *
# * * * *
print('\n3c: N*N-es háromszög kiíratása adott karakterből')
n = int(input('n: '))
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()
# A feladatban láthatjuk, hogy több for ciklus van egymásba ágyazva.  Az első ciklus 0-3 ig megy, ez felelős a sorokért.
# A másik ciklus pedig 0-tól a külsö ciklus i értéke +1 ig megy. Tehát ha a külső érték(i) 0 akkor a belső érték(j) 1 ig megy.
# Tehát minden sor értéke növekszik, így mindig több csillag érték kerül kiíratásra.
# Python lehetőséget ad egy könyebb megoldásra is :D 

print('\n3c 1.2: N*N-es háromszög kiíratása adott karakterből rövidebben')
n = int(input('n: '))
for i in range(n):
    print('* '*(i+1))
# A megoldás alapja hasonló mint alőbb, csak most egy ciklusunk van. A cikluson belűl pedig egy szórzás művelet látható.
# Fontos, ha stringet szorzunk, akkor egymás mellé rakjuk annyiszor, amennyivel beszoroztuk.