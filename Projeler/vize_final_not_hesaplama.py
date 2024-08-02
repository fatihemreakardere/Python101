#vize-final geçme notu hesaplama

#Koşulu yazdırıyoruz
print("Merhaba, bu sistemde vize notunuz %40 final notunuz %60 etkilemektedir ve geçme notu 60'tır.")

#İsim ve notları alıyoruz
ogrenci_adi = input("Lütfen adınızı giriniz: ")
vize_notu = float(input("Lütfen vize notunuzu girin: "))
final_notu = float(input("Lütfen final notunuzu girin: "))

# final notunun %60'ını ve vize notunun %40'ını alarak genel notu hesaplıyoruz.
genel_not = final_notu * 0.6 + vize_notu * 0.4

# genel notu stringe dönüştürerek ekrana yazdırıyoruz.
print("Merhaba " + ogrenci_adi + ", genel notunuz: " + str(genel_not))


# genel notun 60 olup olmadığını kontrol ediyoruz, 60 ve üzeri ise öğrenci geçer, değilse kalır.
if genel_not >= 60.0:
    print("Tebrikler, dersten geçtiniz!")
else:
    print("Üzgünüz, dersten kaldınız.")