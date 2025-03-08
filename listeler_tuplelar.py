# 1. Görev: Kullanıcıdan 5 adet sayı alarak listeye ekleme ve istatistiksel bilgileri bulma
sayilar = []
for i in range(5):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print(f"Liste: {sayilar}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En Büyük: {en_buyuk}")
print(f"En Küçük: {en_kucuk}")

# 2. Görev: Kullanıcıdan aldığı kelimeleri listeye ekleyip ters sıralama
kelimeler = []
for i in range(5):
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelimeler.append(kelime)

kelimeler.reverse()  # Listenin ters sıralanması
print("Ters sıralanmış kelimeler:", kelimeler)

# 3. Görev: Bir liste içindeki tekrar eden elemanları kaldırma
liste = [1, 2, 3, 2, 4, 5, 6, 4, 3]
print(f"Orijinal liste: {liste}")

benzersiz_liste = list(set(liste))  # set() ile tekrarları kaldır, list() ile tekrar listeye dönüştür
print(f"Benzersiz liste: {benzersiz_liste}")
