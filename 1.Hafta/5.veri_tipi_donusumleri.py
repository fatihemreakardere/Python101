#Veri Tipi Dönüşümleri

ilk_yıl = 2023
ikinci_yıl = "2003"
#yıl_farkı = ilk_yıl - ikinci_yıl
#print(yıl_farkı)

#veri tipi kontrolü için type() fonksiyonu
print(type(ilk_yıl))
print(type(ikinci_yıl))

#bir veriyi integer yapmak için int() fonksiyonu

ikinci_yıl = int(ikinci_yıl)
print(type(ikinci_yıl))

yıl_farkı = ilk_yıl - ikinci_yıl
print(yıl_farkı)

ondalik_sayi = 78.54
print(int(ondalik_sayi))

#bir verisi string yapmak için str() fonksiyonu

sayi1 = 789
sayi2 = 561
print(sayi1 + sayi2)

str_sayi1 = str(sayi1)
str_sayi2 = str(sayi2)
str_toplam = str_sayi1 + str_sayi2
print(str_toplam)
print(type(str_toplam))