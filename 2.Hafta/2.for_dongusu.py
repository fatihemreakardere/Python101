#for döngüsü belli bir gruplandırma içerisindeki her bir elementi isimlendirerek çalışır.

kelime = "Python101"

for harf in kelime:
    print(harf)

#range() fonksiyonu belli bir aralıktaki sayıları belirlemek için kullanılan fonksiyondur.
#Eğer yalnızca bir değer verilirse başlangıç değerini 0 kabul eder.
aralık = range(0,15)
print(aralık)

#for döngülerinde range() fonksiyonu belli bir aralıktaki sayıları döngü içerisinde dödndürmeye yarar

for sayi in range(15):
    print(sayi)

#Örnek

for i in range(16):
    if i % 2 == 0:
        print(i,"Bir çift sayıdır")
    elif i % 1 == 0:
        print(i,"Bir tek sayıdır")