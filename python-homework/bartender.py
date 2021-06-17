# Italkiszolgálás életkor és rendelt fajta vizsgálata alapján

kor = int(input('Kérem adja meg az életkorát: '))
ital = input('Mit inna (sör/kóla)? ')

while ital not in ['kóla','sör']:
    print('csak sört és kólát tudunk adni')
    ital = input('Mit inna (sör/kóla)? ')

if kor < 18 and ital == 'sör':
    print('sajnos nem adhatok')
if kor > 60 and ital == 'kóla':
    print('a koffein megemelheti a vérnyomását')