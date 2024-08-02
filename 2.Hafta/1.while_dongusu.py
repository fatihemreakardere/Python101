#while döngüsü yanına yazılan ifade doğru olduğu sürece devamındaki ifadeleri çalıştırır.

#Aşağıdaki kodlar sonsuz döngüye girecektir!!!
###   i = 1
###   while i <= 7:
###       print("Hello World")
###
###   while True:
###       print("Bilgisayar Çıldırdı")

#while döngüsünün sonsuz bir döngü oluşturmamaıs için kodumuzu bir son belirleyecek şekilde optimize etmeliyiz.

k = 1
while k <=5:
    print("Hello World")
    k += 1

j = 1
while j <= 10:
    print(j * "*")
    j = j+1

#Uygulama örneği , break komutu ve kontrolü döngü içerisinde yapma

gizli_sayı = 8
hak_sayısı = 10

print(hak_sayısı,"kadar hakkın var. Gizli sayıyı bulabilecek misin?")

while True:
    tahmin = int(input(str(hak_sayısı) + " Adet deneme hakkın kaldı. Bir sayı giriniz: "))
    if tahmin == gizli_sayı:
        print("Tebrikler!!! Doğru bildin.")
        break
    elif hak_sayısı > 1:
        print("Tekrar dene :(")
        hak_sayısı -= 1
    else:
        print("Kaybettiniz :(")
        break