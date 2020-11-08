# Ötödik óra 2020.11.10.

# Összetett adattípusok

# Tuple
# A tuple egy számokkal indexelhető, nem módosítható lista. Gyakorlatilag hasonló jelenség mint a string, csak itt nem karktereken
# tudunk végig haladni, hanem a tömb egyes elemein. Az indexelés 0-tól kezdödik, és az elemszám-1 ig tart. Az elemeknek nem kell
# azonos típusuaknak lennie, tehát lehet az, hogy három darab egész szám és egy string van tárolva egy tupleön belül.

# 1a Hozzunk létre egy t nevű tuple változót, ami 3 db egész számot tartalmaz, majd irassuk ki.
print ('1a')
t = (100,200,300)
print (t)

# 1b Határozzuk meg a típust, és irassuk ki a képernyőre.
print ('\n1b')
print (type(t))

# 1c Írassuk ki a képernyőre a tuple elemeinek számát.
print ('\n1c')
num_of_elements = len(t)
numOfElements = num_of_elements
print (numOfElements)

# 1d Írassuk ki a tuple második elemét.
print ('\n1d')
print (t[1])

# 1e Próbáljuk ki mi történik túlindexelés esetén.
print ('\n1e')
#print (t[3])

# 1f Módosítsuk az első értéket 100-ról 10-re
print ('\n1f')
#t[0]=10
print (t)

# 1g Tároljunk el egy t nevű változóba három számot és egy stringet
print ('\n1g')
t = (10,'alma',1.0,0.0009)
print (t)

# 1h Hozzon létre egy gyümölcsöket tartalmazó fruits nevű tuple változót, majd ellenőrizze, hogy kérjen be a felhasználotól egy
# gyümölcsöt, és ellenőrizze tartalmazza e a tuple.
print ('\n1h')
fruits = ('körte', 'alma', 'dinnye')
fruit = input('Kérek egy gyümölcsöt: ')
if (fruit in fruits):
    print (fruit,' értéket tartalmazza a fruits tuple')
else:
    print (fruit,'nem része a tuple változónak')

# 1i Hozzon létre egy üres tuple változót aminek legyen empty a neve, és irassa ki típusát
print ('\n1i')
empty = ()
print (type(empty))

# 1j A just_one_element változóban tárolja el a 42 es értéket.
print ('\n1j')
just_one_element = (42)
print (type(just_one_element))

just_one_element = (42,)
print (type(just_one_element))

# List
# A lista a tuple módosítható változata. Tudunk új element hozzáadni, valamint az indexelt elemeket módosítni, szintén nincs
# megkötés az elemek típusára.

# 2a Hozzunk lére egy lista nevű listaváltozót és tároljuk el benne négy egész számot. Írassuk ki a listát, és a típust
print ('\n2a')
lista = [1,2,3,4]
print (lista)
print (type(lista))

# 2b Írassa ki a listaváltozó negyedik elemét, majd módosítsa 5-re és irassa ki a teljes listát
print ('\n2b')
print (lista[3])
lista[3]=5
print (lista)

# 2c Hozzunk létre egy citys nevű változót, tároljunk el benne 4 várost, írassuk is ki. Kérjen be a felhasználotól ezek után
# egy várost, majd adja hozzá a listához és írassa ki.
print ('\n2c')
citys = ['Bécs','Budapest','Brüsszel','Berlin']
print (citys)
newCity = input('Kérek egy várost: ')
citys.append(newCity)
print (citys)

# 2d Szúrjunk be a city listának harmadik helyére még egy város nevét. Majd írassuk ki a megváltozott lista tartalmát
print ('\n2d')
citys.insert(2,'Bangkok')
print (citys)

# 2e Ellenőrizzük, hogy a lista tartalmazza e Budapestet.
print ('\n2e')
if ('Budapest' in citys):
    print ('Igen tartalmazza!')
else:
    print ('Nem tartalmazza!')

# 2f Töröljük kia a lista harmadik elemét, viszont jelenítsük meg a törölt elemet, és az új listát is.
print ('\n2f')
city = citys[2]
print ('A törölt elem a listából:',city)
citys.pop(2)
print (citys)

# 2e Töröljük ki a lista utolsó elemét, majd írjuk ki a listát
print ('\n2e')
citys.pop()
print (citys)

# 2f Hozzunk létre egy nums nevű üres változót, majd töltsük fel 1- től 10-ig az egész számokkal.
print ('\n2f')
nums = []
for i in range(1,11):
    nums.append(i)
print (nums)
