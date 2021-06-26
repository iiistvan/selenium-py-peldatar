# adat.txt beolvasása és kiírása egy sorba

with open("adat.txt", "r") as file1:
    print(" ".join(file1.read().splitlines()))