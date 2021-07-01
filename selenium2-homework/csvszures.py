# csv fájl beolvasás, szűrés, kiiratás egy másik fájlba

import csv

with open('table_in.csv', "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # ciklus a felesleges oszlopok eltávolítására soronként
    for sor in csvreader:
        del sor[2:4]
        # ciklus a soreleji whitespace-ek eltávolítására
        for i in range(len(sor)):
            sor[i] = "".join(sor[i].lstrip())
            # fájl kiirása
        with open('table_out.csv', "a") as csvfile2:
            csvfile2.write(sor[1])
            csvfile2.write(",")
            csvfile2.write(sor[0])
            csvfile2.write("\n")
    csvfile2.close()
