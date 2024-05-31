def bevezeto(nev, koveto, like):
    print("Üdvözöllek a Tiktok-adatkezelő bázisában!")

    while True:
        print("\nVálassz egy lehetőséget:")
        print("1. Adat rögzítése")
        print("2. Statisztikák megtekintése")

        valasz = input("Választásod: ")

        if valasz == "1":
            adat_rogzitese()
        elif valasz == "2":
            statisztikak_megtekintese(nev, koveto, like)
        else:
            print("Érvénytelen választás. Kérlek, válassz újra.")

def adat_rogzitese():
    print("\nKiválasztottad az Adatok rögzítése opciót.")
    melyik_f = input("Melyik fájlba szeretnél rögzíteni? (be1 / be2) ")
    
    while not melyik_f == "be1" or melyik_f == "be2":
        print("\nÉrvénytelen fájl! Érvényes: (be1 / be2) ")
        melyik_f = input("Add meg a fájlt, amibe rögzíteni szeretnél: ")

    file = open(f"{melyik_f}.txt", "a", encoding="UTF-8")
    print("Minta: str - int - int")
    line = input("Add meg az adatot amit rögzíteni szeretnél ")
    file.write(f"{line}\n")
    akar_e = input("\nSzeretnél többet írni? (i/n) ")
    if akar_e == "i":
        adat_rogzitese()


def statisztikak_megtekintese(nev, koveto, like):
    print("\nKiválasztottad a  Statisztikák megtekintése opciót.")
    print(f"\n\n1) Tiktokkerek száma, akiknek több mint 20.000.000 követője van: {megszamolas(koveto)}")
    print(f"\n2) Tiktokkerek követőinek átlaga: {osszegzes(koveto)}")
    print(f"\n3) Legalacsonyabb követővel rendelkező tiktokker: {legkevesebb(koveto)}")

def beFajl(nev, koveto, like):
    fr = open("be1.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    tiktokker = []
    while sor != "":
        darabolt = sor.split(" - ")
        nev.append(darabolt[0])
        koveto.append(int(darabolt[1]))
        like.append(int(darabolt[2]))
        sor = fr.readline().strip()
    fr.close()


def megszamolas(koveto):
    db = 0
    for i in range(len(koveto)):
        if koveto[i] > 20000000:
            db += 1
    return db


def leghiresebb(x):
    maxi = 0
    for i in range(1, len(x)):
        if x[i] > x[maxi]:
            maxi = i
    return maxi

def legkevesebb(x):
    mini = 0
    for i in range(1, len(x)):
        if x[i] < x[mini]:
            mini = i
    return mini

def kereses(nev, koveto, like):
    ...

def rendez(x, y):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1):
            if y[j] > y[j+1]:
                y[j], y[j+1] = y[j+1], y[j]
                x[j], x[j+1] = x[j+1], x[j]

def osszegzes(koveto):
    s = 0
    for i in range(len(koveto)):
        s += koveto[i]
    atlag = (s/len(koveto), 2)
    return atlag

def HUNosszegzes(nev, koveto, like):
    ...

def kivalogatas(nev, koveto, like):
    ...

def main():
    nev, koveto, like = [], [], []
    bevezeto(nev, koveto, like)
    # Összes fgv megadása?

main()