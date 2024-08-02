# Basit Hesap Makinesi

# Kullanıcıdan iki sayı ve işlemi al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("İşlemi girin (+, -, *, /): ")

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