# Szökőév vizsgálat

def szokoevSzamolo(ev):
    if ev % 400 == 0:
        szokoev = True
    elif ev % 100 == 0:
        szokoev = False
    elif ev % 4 == 0:
        szokoev = True
    else:
        szokoev = False
    return (szokoev)

folytat = 'i'
while folytat == 'i':
    szev = int(input('Kérem az évszámot: '))
    szoko = szokoevSzamolo(szev)
    if szoko:
        print('Szökőév')
    else:
        print('Nem szökőév')
    print()
    folytat = input('Újabb számolás (i/n)?')
