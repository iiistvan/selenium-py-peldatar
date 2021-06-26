# adat.txt beolvasása és tárolása listába, majd kiírása egy sorként, egy másik fájlba

with open("adat.txt", "r") as file1:
    szoveg = file1.read().splitlines()
with open("adat2.txt", "a") as file2:
    file2.write(" ".join(szoveg))