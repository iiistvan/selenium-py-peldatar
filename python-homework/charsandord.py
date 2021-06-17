# angol abc kisbetűinek kiiratása max. 10 sorból álló oszlopokba

for dec in range(97,107):
    print(chr(dec), dec, end='  ')
    masodik = dec+10
    print(chr(masodik), masodik, end='  ')
    harmadik = dec+20
    if harmadik > 122:
        print()
        continue
    print(chr(harmadik), harmadik, '  ')