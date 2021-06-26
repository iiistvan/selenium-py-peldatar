# adat.txt beolvasása és tárolás nélküli kiirása másik fájlba

with open("adat.txt", "r") as file1:
    with open("adat4.txt", "a") as file2:
        file2.write(file1.read())