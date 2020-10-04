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

# 1b A közlekedési hatóság számára kell egy olyan programot készítenünk, amely meghatározza, hogy adott koru személy számára
# milyen típusú jogosítványok adhatoak ki. A kor bekérésekor figyeljünk arra, hogy engedélyezett a 22.5 beírás pl. tehát nem csak
# egészek adhatóak meg!
# Jogosítvány kategóriák:
# A -> 23.5 év
# AM -> 15.5 év
# B -> 17 év
print('\n1b : Jogosítvány megszerzése')

# 1c Egy jelszó ellenörző programot készítünk. A döntésünk alapja, hogy megfelelő e, a jelszó, a hossza.
# Kérjen be a felhasználótól egy 8-16 karakter hosszú jelszót. Következő ellenörzési feltételek valósuljanak meg:
# - 0-7 karakter - Túl rövid! Nem elfogadhtató!
# - 8-10 karakter - Alacsony biztonság!
# - 11-14 karakter - Közepes biztonság!
# - 15-16 karakter - Magas biztonság!
# - 16+ Túl hosszú! Nem elfogadható!
print ('\n1c : Jelszó ellenőrzés')

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
print('\n2a : Dolgozat ellenőrzés')


# 2b Készítsen egy jelszó ellenőrző progrmot, amely mind addig fog bekérni jelszót a felhaszbálótól,
# ameddig az megfelelő nem lesz. Az a jelszó megfelelő, amelyik minimum 10 karakter hosszú, maximum 32.
# Ha nem megfelelő a jelszó erről tájékoztassuk a felhasználót, és ugynúgy az elfogadott jelszó tényéről is.
print('\n2b: Jelszó ellenőrzés')

#2c Készítsünk egy számkitalálós játékot. A programunk véletlenszerűen generáljon egy egész számot 1 és 100 között. Majd kérjen be a
# felhasználótól is egy egészet. Ha megyegyezik a kettő a user nyert, ha nincs egyezés, írjuk ki, hogy a tipp kisebb vagy nagyobb
# mint a kisorsolt szám, és kérjünk be egy új tippet.
print('\n2c: Számkitalálós játék')
import random
num = random.randint(1,100)

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

# 3a Írassuk ki a felhasználó által megadott pozitív egész számig, a számok négyzetét.
print('\n\n3a: négyzetszámok kiíratása')

# 3b Kérjünk be a felhasználótól egy nevet. Majd írjuk ki, egyesével a betűit egymás alá az adott névnek.
print('\n\n3b: Név betűinek kiíratása')

# 3c n-szer n-es hárömszög kiíratása * karakterekből
# Példa:
# n: 4
# *
# * *
# * * *
# * * * *
print('\n3c: N*N-es háromszög kiíratása adott karakterből')


print('\n3c 1.2: N*N-es háromszög kiíratása adott karakterből rövidebben')
