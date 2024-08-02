# Basit Hesap Makinesi (While Döngüsü İle Birlikte)

#Bu örneği yapabilmek için daha önce if ifadesiyle yaptığımız örneğe döngülerle birlikte istediğimiz kadar işlem yapabilme yeteneği katıyoruz

while True: #Burada sonsuz bir döngü açıyoruz. Dolayısıyle koşullu durumlar içerisinde döngüden çıkma komutu eklememiz gerekecek

    # Kullanıcıdan iki sayı ve işlemi al
    islem = input("İşlemi girin (+, -, *, /), çıkmak için 'q': ")

    if islem == "q": #Bu ifade ile kullanıcı eğer programdan çıkmak istiyorsa döngünün sonlanmasını sağlıyoruz
        print("Programdan çıkılıyor...")
        break

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))


    # Seçilen işlemi gerçekleştir
    if islem == '+':
        sonuc = sayi1 + sayi2
    elif islem == '-':
        sonuc = sayi1 - sayi2
    elif islem == '*':
        sonuc = sayi1 * sayi2
    elif islem == '/':
        sonuc = sayi1 / sayi2
    else:
        print("Geçersiz işlem")
        sonuc = "gecersiz"

    # Sonucu yazdır
    if sonuc != "geçersiz":
        print("Sonuç: " + str(sonuc))