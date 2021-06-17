# 10 alatti számok beolvasása és összegzése

szam = osszeg = 0
type(osszeg)
while szam < 10:
    osszeg += szam
    szam = int(input('Kérem a számot: '))
print('A 10 alatti számok összege: ',osszeg)

