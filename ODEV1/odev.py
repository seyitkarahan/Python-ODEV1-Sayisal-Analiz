import math


x = math.pi / 5

# ilk terminin hesaplanması

cos_hesaplanan_deger1 = 1

cos_gercek_deger1 = math.cos(x)

kesme_hatasi = (cos_gercek_deger1 - cos_hesaplanan_deger1)

print(f"Hesaplanan Değer: {cos_hesaplanan_deger1}")
print(f"Gercek Değer: {cos_gercek_deger1}")
print(f"Kesme Hatası: {kesme_hatasi}")


print("--------------------------------------------------------")

# ilk iki teriminin hesaplanması

cos_hesaplanan_deger2 = 1 - (x ** 2) / 2

cos_gercek_deger2 = math.cos(x)

kesme_hatasi2 = (cos_gercek_deger2 - cos_hesaplanan_deger2)

print(f"Hesaplanan Değeri: {cos_hesaplanan_deger2}")
print(f"Gerçek Değeri: {cos_gercek_deger2}")
print(f"Kesme Hatası: {kesme_hatasi2}")
