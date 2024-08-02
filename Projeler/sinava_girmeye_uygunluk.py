#Sınava Girmeye Uygunluk

#Öncelikle sınava girmeye uygun olan adayların isimlerini depolayacağımız boş bir isim listesi oluşturuyoruz

isim_listesi = []

#Daha sonrasında ise son isim girildikten sonra kapatmak üzere while döngüsü oluşturuyoruz

while True: #Sonsuz bir döngü oluşturduğumuz için bu döngüyü daha sonra bitirmeliyiz
    #Kullanıcıdan isim ve yaş bilgilerini alıyoruz

    isim = input("Adınızı giriniz (Eğer işlem tamamlandıysa 'quit' yazınız): ")

    if isim == "quit": #Eğer programın bir noktasında isim yerine çıkış komutu verilirse programı sonlandırıyoruz ve listemizi yazdırıyoruz.
        print("İşlem tamamlandı. Sınava girmeye uygun adaylar listesi:",isim_listesi)
        break
    else:
        yas = int(input("Yaşınızı giriniz:"))
        if yas >= 18: #Eğer sınav adayımız 18 yaşından büyükse girdiği ismi listemize ekliyoruz.
            isim_listesi.append(isim)