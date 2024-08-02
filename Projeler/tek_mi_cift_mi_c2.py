#Önce listeler tanımlanır
sayi_listesi = [2,5,4,8,1,17,9,5,7,6,3,789,54,322,12,242]

cift_sayilar = []

tek_sayilar = []

#Daha sonrasonda for döngüsü ile liste içerisinde dolaşıp koşullu durumlarla yeni listeler oluşturulur.

for i in range(len(sayi_listesi)):
    if sayi_listesi[i] % 2 == 0: #2 ile bölümünden kalan 0'a eşit olan sayılar çifttir
        cift_sayilar.append(sayi_listesi[i])
    elif sayi_listesi[i] % 2 == 1: #2 ile bölümünden kalan 1'e eşit olan sayılar tektir
        tek_sayilar.append(sayi_listesi[i])

#Sonucu çıktı alıyoruz
print("Çift sayı listesi: ", cift_sayilar)
print("Tek sayı listesi: ", tek_sayilar)