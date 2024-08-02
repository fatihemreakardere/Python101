#Şimdi de for döngüsü yardımıyla bir faktöriyel fonksiyonu tanımlayalım.

def faktoriyel(x):
    sonuc = 1 #Öncelikle faktöriyel fonksiyonumuz için bir başlangıç değeri belirliyoruz.
    for i in range(1,x + 1): #Burada range fonksiyonu yardımıyla x'e kadar olan tüm sayılari i değişkenimize tanımlıyoruz.
        sonuc = sonuc * i
    return sonuc
#Yukarıda range() fonksiyonunu kullanırken başlangıç değerimizi 1 olarak, son değerimizi de x + 1 olarak belirlediğimize dikkat edelim
#range() fonksiyonunda ilk değer aralığı dahilken son değer aralığa dahil değildir
print(faktoriyel(0))