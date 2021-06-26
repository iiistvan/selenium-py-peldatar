# adat.txt beolvasása és tárolása listában, majd kiírása fájlba soronként

with open("adat.txt", "r") as file1:
    szoveg = file1.read().splitlines()
with open("adat3.txt", "a") as file2:
    file2.write("\n".join(szoveg))