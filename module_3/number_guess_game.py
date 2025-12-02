import random

print("1 ile 100 arasında bir sayı tahmin et")

min_sayi = 1
max_sayi = 100

# sistemin arka planda seçtiği sayı
sayi = random.randint(min_sayi, max_sayi)

puan = 100  
adim = 0    

while True:
    tahmin = input(f"\nTahmininiz ({min_sayi}-{max_sayi}): ")
 
    if not tahmin.isdigit():
        print("Lütfen geçerli bir sayı gir.")
        continue
    tahmin = int(tahmin)
    adim += 1
  
    if tahmin == sayi:
        print(f"Tebrikler!")
        print(f"total puanınız: {puan}")
        break
    elif tahmin < sayi:
        print(" Yukarı çık")
        min_sayi = max(min_sayi, tahmin + 1)  
        puan -= 5
    else:
        print("Aşağı in")
        max_sayi = min(max_sayi, tahmin - 1)  
        puan -= 5

    if puan <= 0:
        print("Kaybettiniz!")
        print(f"Doğru sayı: {sayi}")
        break
