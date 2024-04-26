def bevezeto(nev, koveto, like):
    print("Üdvözöllek a Tiktok-adatkezelő bázisában!")

    while True:
        print("\nVálassz egy lehetőséget:")
        print("1. Adat rögzítése")
        print("2. Statisztikák megtekintése")

        valasz = input("Választásod: ")

        if valasz == "1":
            adat_rogzitese(nev, koveto, like)
        elif valasz == "2":
            statisztikak_megtekintese(nev, koveto, like)
        else:
            print("Érvénytelen választás. Kérlek, válassz újra.")

def beFajl(nev, koveto, like):
    fr = open("adatok.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    tiktokker = []
    while sor != "":
        darabolt = sor.split(" - ")
        nev.append(darabolt[0])
        koveto.append(int(darabolt[1]))
        like.append(int(darabolt[2]))
        sor = fr.readline().strip()
    fr.close()

def adat_rogzitese(nev, koveto, like):
    print("\nKiválasztottad az Adatok rögzítése opciót.")

def statisztikak_megtekintese(nev, koveto, like):
    print("\nKiválasztottad a Statisztikák megtekintése opciót.")

def megszamolas(nev, koveto, like):
    ...

def minmax(nev, koveto, like):
    ...

def leghiresebb(x, y):
    ...

def legkevesebb(x, y):
    ...

def kereses(nev, koveto, like):
    ...

def rendez(x, y):
    n = len(x)
    for i in range(n):
        for j in range(n-i-1):
            if y[j] > y[j+1]:
                y[j], y[j+1] = y[j+1], y[j]
                x[j], x[j+1] = x[j+1], x[j]

def osszegzes(x, y):
    s = 0
    for i in range(len(y)):
        s += y[i]
    atlag = (s/len(y), 2)
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