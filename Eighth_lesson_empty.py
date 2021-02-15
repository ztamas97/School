#8. óra 2021.02.02.
# Fájlkezelés

# A fájlok logikailag összetartozó adatok gyűjteménye. A fájlok rendelkeznek egy azonosítóval(first_lesson), valamint kiterjesztéssel(.pdf,.docx,.py).
# Ennek megkötéseit, valamint maximális méretét, és többi paraméterét a fájlrendszer határozza meg.
# Egy fájl életciklusa:
# megnyitás
# olvasás,írás
# bezárás

# 1 Nyissunk meg egy adott elnevezésű szövegfájlt.
print('1. feladat')
f=open('teszt.txt')

# 2 Kérjük le a típusát az elöbb említett változónak, majd írassuk ki típusát.
print('\n2. feladat')
print(type(f))

# 3 Zárjuk be a fájlt.
print('\n3. feladat')
f.close()

# 4 Olvassuk be a teszt.txt fájl tartalmát egy content nevű változóba.
print('\n4. feladat')
f=open('teszt.txt')
content=f.read()
print(content)

# 5 Mindez rövidebben...
print('\n5. feladat')
print(open('teszt.txt').read())

# 6 Olvassunk be csak egyetlen sor a fájlból.
print('\n6. feladat')
f=open('teszt.txt')
row=f.readline()
print(row)

# 8 Írassuk ki az első sort utána sortörtés nélkül.
print('\n8. feladat')
f=open('teszt.txt')
row=f.readline().strip()
print(row)

# 9 Olvassuk be a listába a sorokat.
print('\n9. feladat')
f=open('teszt.txt')
row=f.readlines()
print(row)

# 10 Iteráljunk végig a fájl sorain, és írassuk ki azokat.
print('\n10. feladat')
for i in open('teszt.txt').readlines():
    print(len(i))
    
# 11 Írassuk ki egy numbers.txt nevű fájlba a számokat 0-tól 10-ig
print('\n11. feladat')
nf=open('numbers.txt','a')
for i in range(0,11):
    nf.write(str(i))
    nf.write('\n')
nf.close()
    