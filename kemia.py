#  Év;    Elem;      Vegyjel;     Rendszám;        Felfedező'
#  0         1           2            3                 4
      
with open("felfedezesek.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [sor.strip().split(";") for sor in f]


print(f"3.feladat: Elemek száma: {len(lista)}")

okor = len([sor for sor in lista if sor[0] == "Ókor"])

print(f"4.feladat: Felfedezések száma az ókorban: {okor}")

while True:
    bekeres = input("5.feladat: Kérek egy vegyjelet: ")
    if len(bekeres) == 1 or len(bekeres) == 2 and bekeres.isalpha():
        break

vegyjel_kereso = [sor for sor in lista if bekeres.lower().capitalize() in sor[2]]

#vegyjel.nev,rendszam,felfedezeseve,felfedezo

if len(vegyjel_kereso) > 0:
    [print(f"""6.feladat: Keresés:
       Az elem vegyjele: {sor[2]}
       Az elem neve: {sor[1]}
       Rendszám: {sor[3]}
       Felfedezés éve: {sor[0]}
       Felfedező: {sor[4]}""") for sor in vegyjel_kereso]   #  ༼ つ ◕_◕ ༽つ
else:
    print("       Nincs ilyen elem az adatforrásban!")
    
# 7-es feladat passz

print("7.feladat: --")

statisztika = dict()
print("8.feladat: Statisztika")
for sor in lista:
    ev = sor[0]
    statisztika[ev] = statisztika.get(ev, 0) + 1
evek = [ print(f' {ev}: {db} db.') for ev, db in statisztika.items() if db > 3 and ev != "Ókor"]
