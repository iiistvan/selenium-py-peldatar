# adat.txt beolvasása és tárolása listában, majd kiírása egy sorba

with open("adat.txt", "r") as file1:
    szoveg = file1.read().splitlines()
    print(" ".join(szoveg))