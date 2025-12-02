desen = input("Sembol seç ")
n = int(input("Kaç satırlık olsun? "))
print(f"\n{desen} Deseniniz:")

for i in range(1, n + 1):
    print(desen * i)
