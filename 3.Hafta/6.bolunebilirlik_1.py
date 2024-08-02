#Bölünebilirlik - 1
#Kullanıcıdan bir sayı alıp bu sayının hem 3'e hem de 7'ye tam bölünüp bölünmediğini döndüren bir fonksiyon yazınız

def bolunebirlilik_1() :
    sayi = int(input("Bir sayı giriniz: "))
    if sayi % 21 == 0:
        print(sayi,"sayısı hem 3'e hem de 7'ye tam bölünebilir.")
    else :
        print(sayi,"sayısı 3'e ve 7'ye aynı anda kalansız olarak bölünemez.")


bolunebirlilik_1()