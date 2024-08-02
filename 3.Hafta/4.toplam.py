#Return ifadesi
#Bu ifade fonksiyon içerisinde bir değer döndürmemizi sağlar
#Örnek

def toplam(x,y):
    return x + y

toplam(5,15)

#Yalnızca yukarıdaki şekilde fonksiyonu çağırmak bu sefer çıktı almamız için yeterli olmayacaktır
#Bu fonksiyonumuzda diğerlerinden farklı olarak bir print() fonksiyonu kullanmadık
#Yukarıdaki ifadeyi ekranımızda yazdırmak için kendimiz print() fonksiyonu içerisine koymalıyız

print(toplam(5,15))

#Aynı zamanda return ifadesiyle birlikte fonksiyonumuz bir değer döndürdüğü için, fonksiyonumuzun sonucunu bir değişkene tanımlayabiliriz.

sayilarin_toplami = toplam(45,85)
print(sayilarin_toplami)

#Şimdi de çıkartma ve çarpım fonksiyonlarını kendimiz yazmaya çalışalım...