#bir stringin uzunluğunu bulmak için len() fonksiyonu

cumle = "Bu 30 karakterli bir stringtir"
print(cumle)
print(len(cumle))

#bir stringin tüm karakterlerini büyük harfe dönüştürmek için .upper() methodu

cumle_iki = "bu, tüm karakterleri küçük bir cümledir."
print(cumle_iki.upper())

#bir stringin tüm karakterlerini büyük harfe dönüştürmek için .upper() methodu

cumle_uc = "BU, TÜM KARAKTERLERİ BÜYÜK BİR CÜMLEDİR."
print(cumle_uc.lower())

#bir stringin diğer bir string içerisinde kaç kez olduğunu saymak için .count() methodu

cumle_dort = "bu cümlede beş tane 'a' ve 1 tane 'A' karakteri geçer."
print(cumle_dort.count("a"))
print(cumle_dort.count("A"))

#girdili örnek

girdi_cumle = input("Bir cümle girini: ")
karakter_girdi = input("Bir karakter giriniz: ")
karakter_sayac = girdi_cumle.count(karakter_girdi)
cumle_uzunlugu = len(girdi_cumle)
print(str(cumle_uzunlugu) + " karakterli '" + girdi_cumle + "' cümlesinde '" + karakter_girdi + "' karakteri " + str(karakter_sayac) + " kez geçer.")

#stringde index mantığı
# "örnek"
#  01234
#indexler her zaman 0'dan başlar ve artarak devam eder.

kelime = "örnek"
kelime_index_0 = kelime[0]
print(kelime + " kelimesinin ilk indexi (0. index) '" + kelime_index_0 + "' karakteridir")

#bir stringin diğer bir string içerisinde bulunduğu ilk indexi bulmak için .index() metodu

print(kelime.index("r"))