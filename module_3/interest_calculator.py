ana_para = float(input("Ana paranızı girin: "))
faiz_orani = float(input("Yıllık faiz oranı: "))
yil_sayisi = int(input("Kaç yıl: "))

bakiye = ana_para
for yil in range(1, yil_sayisi + 1):
    bakiye = bakiye * (1 + faiz_orani / 100)
    print(f"{yil:3} | {bakiye:,.2f}")

total_faiz = bakiye - ana_para
print(f"\nTotal kazancınız: {total_faiz:,.2f}")
