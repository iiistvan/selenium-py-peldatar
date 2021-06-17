# Benzinköltségszámoló progi

def adatbeker():
    varosiFogy = float(input('A városi fogyasztás (l/100km):   '))
    orszagutiFogy = float(input('Az országúti fogyasztás (l/100km): '))
    varosiTav = float(input('A városban megett távolság (km):   '))
    orszagutiTav = float(input('Az országúton megett távolság (km):   '))
    arBenzin = float(input('A benzin ára (Ft):   '))
    print('A megetett út költsége: ', (varosiTav * varosiFogy + orszagutiTav * orszagutiFogy) * arBenzin / 100)


# utiköltség számolása fix adatokkal
odautKoltseg = (9*35+7*170)*350/100
print('Az oda út költsége: ', odautKoltseg)
print('Az oda-vissza út költsége: ', odautKoltseg*2)
print()

# utiköltség számolása bekért adatokkal
folytat = 'i'
while folytat == 'i':
    adatbeker()
    folytat = input('Újabb számolás (i/n)?')
    print()
