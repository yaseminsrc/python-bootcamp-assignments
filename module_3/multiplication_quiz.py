import random

soru_sayisi = 5
puan = 0

for i in range(1, soru_sayisi + 1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
       cevap = input(f"Soru {i}: {a} x {b} = ")
    
    if not cevap.isdigit():
        print("puan kazanamadın")
        continue
    
    cevap = int(cevap)
    if cevap == a * b:
        print("Doğru bildiniz")
        puan += 10
    else:
        print(f" Cevap Yanlış. Doğru cevap: {a * b} olmalıydı")

print(f"\nOyun bitti! Toplam puanın: {puan}/{soru_sayisi * 10}")
