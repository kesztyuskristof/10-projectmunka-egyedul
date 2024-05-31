from random import *

# Beolvasás
def beFajl(nev, koveto, like):
    melyik_f = input("\nAdd meg a fájlt, amivel dolgozni szeretnél: (be1 / be2) ")
    
    while melyik_f != "be1" and melyik_f != "be2":
        print("\nÉrvénytelen fájl! Érvényes: (be1 / be2)")
        melyik_f = input("Kérlek adj meg egy érvényes fájlt: ")

    fr = open(f"{melyik_f}.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        darabolt = sor.split(" - ")
        nev.append(darabolt[0])
        koveto.append(int(darabolt[1]))
        like.append(int(darabolt[2]))
        sor = fr.readline().strip()
    fr.close()

# Bevezető
def bevezeto(nev, koveto, like):
    print("Üdvözöllek a Tiktok-adatkezelő bázisában!")

    print("\nVálassz egy lehetőséget: ")
    print("1. Adat rögzítése")
    print("2. Statisztikák megtekintése")
    print("3. Név alapján keresés")
    print("+. Dobókocka :O")

    valasz = input("Választásod: ")

    if valasz == "1":
        adat_rogzitese()
    elif valasz == "2":
        beFajl(nev,koveto,like)
        statisztikak_megtekintese(nev, koveto, like)
    elif valasz == "3":
        beFajl(nev,koveto,like)
        nev_kereses(nev, koveto, like)
    elif valasz == "+":
        dobokocka()
    else:
        print("\nÉrvénytelen választás!")

# Adatrögzítés
def adat_rogzitese():
    print("\nKiválasztottad az Adatok rögzítése opciót.")

    melyik_f = input("Add meg a fájlt, amibe rögzíteni szeretnél: (be1 / be2) ")
    while melyik_f != "be1" and melyik_f != "be2":
        print("\nÉrvénytelen fájl! Érvényes: (be1 / be2)")
        melyik_f = input("Add meg a fájlt, amibe rögzíteni szeretnél: ")
    
    print("\nMinta: str - int - int")

    fa = open(f"{melyik_f}.txt", "a", encoding="UTF-8")
    line = input("Add meg az adatot amit rögzíteni szeretnél: ")
    fa.write(f"{line}\n")
    fa.close()

    print(f"\n\nSikeres adatrögzítés! Nézd meg a {melyik_f}.txt fájlt!")

# Statisztikák
def statisztikak_megtekintese(nev, koveto, like):
    print("\nKiválasztottad a Statisztikák megtekintése opciót.")
    print(f"\n\n1) Tiktokkerek száma, akiknek több mint 25.000.000 követője van: {megszamolas(koveto)}")
    print(f"\n2) Tiktokkerek követőinek átlaga: {osszegzes(koveto)}")
    
    min_index = legkevesebb(koveto)
    print(f"\n3) Legalacsonyabb követővel rendelkező tiktokker: {nev[min_index]}")

    max_index = leghiresebb(koveto)
    print(f"\n4) Legtöbb követővel rendelkező tiktokker: {nev[max_index]}")

    print(f"\n5) Azoknak a TikTokkereknek a nevei akiknek több mint 3.000.000.000 lájkja van: {kivalogatas(nev, like)}")

    rendez(nev, koveto)
    print(f"\n6) TikTokkerek nevei rendezve növekvő sorrendben követők száma alapján: {nev}")


# Programozási tételek (+ Gamba):


# 1) Megszámolás
def megszamolas(koveto):
    db = 0
    for i in range(len(koveto)):
        if koveto[i] > 2500000:
            db += 1
    return db

# 2) Összegzés
def osszegzes(koveto):
    s = 0
    n = len(koveto)
    for i in range(n):
        s += koveto[i]
    return s/len(koveto)

# 3) Minimum
def legkevesebb(x):
    mini = 0
    for i in range(1, len(x)):
        if x[i] < x[mini]:
            mini = i
    return mini

# 3.2) Maximum
def leghiresebb(x):
    maxi = 0
    for i in range(1, len(x)):
        if x[i] > x[maxi]:
            maxi = i
    return maxi

# 4) Keresés
def nev_kereses(nev, koveto, like):
    print("\nKiválasztottad a Név alapján keresés opciót.")
    keresett_nev = input("Add meg a TikTokker nevét akit keresel: ")
    i = 0
    n = len(nev)
    while i < n and not(keresett_nev == nev[i]):
        i += 1
    if i < n:
        print(f"\nA keresett TikTokker adatai: {nev[i]} - {koveto[i]} - {like[i]}")
    else:
        print("\nNincs ilyen tiktokker! Kérlek, próbáld újra ")

# 5) Kiválogatás
def kivalogatas(nev, like):
    y = []
    for i in range(len(nev)):
        if like[i] > 3000000000:
            y.append(nev[i])
    return y

# +) Dobókocka
def dobokocka():
    kocka = randint(1, 6)
    print(f"Ennyit dobtál: {kocka}")

# 6) Rendezés
def rendez(x, y):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1):
            if y[j] > y[j+1]:
                y[j], y[j+1] = y[j+1], y[j]
                x[j], x[j+1] = x[j+1], x[j]


def main():
    nev, koveto, like = [], [], []
    bevezeto(nev, koveto, like)

main()