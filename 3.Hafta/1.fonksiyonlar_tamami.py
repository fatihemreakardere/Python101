#Fonksiyonlar
#Python'da fonksiyonlar, belirli bir işlevi gerçekleştirmek için kullanılan bloklar halindeki kod parçacıklarıdır.
#Fonksiyonlar, kodunuzu daha modüler hale getirerek tekrar kullanılabilirliği artırır ve kodunuzu daha okunabilir kılar.
#Fonksiyonlar içerisinde başka fonksiyonlar da kullanabiliriz.

#Örnek ve ilk fonksiyonumuz
def hello_world():
    print("Hello World")

#Fonksiyonu aşağıdaki şekilde çağırarak kullanıyoruz.
hello_world()

#Bir fonksiyonu birden fazla kez çağırabiliriz. (# işaretlerini kaldırarak deneyebilirsiniz)
#hello_world()
#hello_world()
#hello_world()
#hello_world()
#hello_world()

#Daha önceden isim bilgisi ile print fonksiyonu yardımıyla kullanıcıya selam verebilmiştik.
#Şimdi bunu Selam fonksiyonunu kendimiz yazarak yapalım.
#Fonksiyonlar, girdi değerleri alabilir. Bu değerler, fonksiyonun işlem yapması için gerekli bilgileri sağlar.
#Bunlara parametre adı veririz

def Selam(isim):
    print("Merhaba", isim, "tanıştığımıza memnun oldum.")
ad = "James Bond"
Selam(ad)

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

#Şimdi de for döngüsü yardımıyla bir faktöriyel fonksiyonu tanımlayalım.

def faktoriyel(x):
    sonuc = 1 #Öncelikle faktöriyel fonksiyonumuz için bir başlangıç değeri belirliyoruz.
    for i in range(1,x + 1): #Burada range fonksiyonu yardımıyla x'e kadar olan tüm sayılari i değişkenimize tanımlıyoruz.
        sonuc = sonuc * i
    return sonuc
#Yukarıda range() fonksiyonunu kullanırken başlangıç değerimizi 1 olarak, son değerimizi de x + 1 olarak belirlediğimize dikkat edelim
#range() fonksiyonunda ilk değer aralığı dahilken son değer aralığa dahil değildir
print(faktoriyel(0))

#Bölünebilirlik - 1
#Kullanıcıdan bir sayı alıp bu sayının hem 3'e hem de 7'ye tam bölünüp bölünmediğini döndüren bir fonksiyon yazınız

def bolunebirlilik_1() :
    sayi = int(input("Bir sayı giriniz: "))
    if sayi % 21 == 0:
        print(sayi,"sayısı hem 3'e hem de 7'ye tam bölünebilir.")
    else :
        print(sayi,"sayısı 3'e ve 7'ye aynı anda kalansız olarak bölünemez.")


bolunebirlilik_1()

#Bölünebilirlik - 2
#Kullanıcıdan bir sayı alalım. Bu sayı;
#   Eğer 3'e tam bölünebiliyor ama 7'ye tam bölünemiyorsa 1,
#   Eğer 7'ye tam bölünebiliyor ama 3'e tam bölünemiyorsa 2,
#   Eğer hem 7'ye hem de 3'e tam bölünüyorsa 3 sayısını çıktı olarak verelim.
#   Eğer girilen sayı yukarıdaki hiçbir kuralı sağlamıyorsa "hmm, çok ilginç bir sayı girdiniz..." çıktısı alalım.

def bolunebilirlik_2():
    sayi = int(input("Bir sayı giriniz: "))
    if sayi % 3 == 0 and sayi % 7 != 0 :
        print(1)
    elif sayi % 7 == 0 and sayi % 3 != 0 :
        print(2)
    elif sayi % 21 == 0 :
        print(3)
    else:
        print("hmm, çok ilginç bir sayı girdiniz...")

bolunebilirlik_2()