#  Év;    Elem;      Vegyjel;     Rendszám;        Felfedező'
#  0         1           2            3                 4

class Kemia:
    def __init__(self,sor):
        ev,elem,vegyjel,rendszam,felfedezo = sor.strip().split(";")
        self.ev = ev
        self.elem = elem
        self.vegyjel = vegyjel
        self.rendszam = rendszam
        self.felfedezo = felfedezo
        
        
        
with open("felfedezesek.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [Kemia(sor) for sor in f]


print(f"3.feladat: Elemek száma: {len(lista)}")

okor = len([sor for sor in lista if sor.ev == "Ókor"])

print(f"4.feladat: Felfedezések száma az ókorban: {okor}")

while True:
    bekeres = input("5.feladat: Kérek egy vegyjelet: ")
    if len(bekeres) == 1 or len(bekeres) == 2 and bekeres.isalpha():
        break

vegyjel_kereso = [sor for sor in lista if bekeres.lower().capitalize() in sor.vegyjel]

#vegyjel.nev,rendszam,felfedezeseve,felfedezo

if len(vegyjel_kereso) > 0:
    [print(f"""6.feladat: Keresés:
       Az elem vegyjele: {sor.vegyjel}
       Az elem neve: {sor.elem}
       Rendszám: {sor.rendszam}
       Felfedezés éve: {sor.ev}
       Felfedező: {sor.felfedezo}""") for sor in vegyjel_kereso]   #  ༼ つ ◕_◕ ༽つ
else:
    print("       Nincs ilyen elem az adatforrásban!")
    
# 7-es feladat passz

print("7.feladat: --")

statisztika = dict()
print("8.feladat: Statisztika")
for sor in lista:
    ev = sor.ev
    statisztika[ev] = statisztika.get(ev, 0) + 1
evek = [ print(f' {ev}: {db} db.') for ev, db in statisztika.items() if db > 3 and ev != "Ókor"]
