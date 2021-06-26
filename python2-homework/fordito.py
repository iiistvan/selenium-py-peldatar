# egész számok bekérése 0-ig, majd kiírás fordított sorrendben

# változók beállítása
szam, szamok = 1, []

print("Pozitív egész számokat kérek be egészen 0 megadásáig, majd fordított sorrenben kiiratom.", '\n')

# adatbekérés hibakezeléssel
while szam:
    try:
        szam = int(input("Kérem a következő számot: "))
        assert szam > 0
        szamok.append(szam)
    except:
        print("Pozitív egész számot várok!")

# fordított sorrendű kiiratás
print(szamok[::-1])
