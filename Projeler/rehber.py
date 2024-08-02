rehber = []
def kisi_ekle(ad, soyad, tel_no):
    rehber.append({"Ad":ad, "Soyad" : soyad, "Tel_No": tel_no})

def kisi_listele():
    for kisi in rehber:
        print("-"*20)
        print("Adı: ", kisi["Ad"])
        print("Soyadı: ", kisi["Soyad"])
        print("Tel No: ", kisi["Tel_No"])

def kisi_sil(ad,soyad):
    for kisi in rehber:
        if (kisi["Ad"] == ad) and (kisi["Soyad"] == soyad):
            rehber.remove(kisi)

def kisi_guncelle(ad, soyad):
    for kisi in rehber:
        if (kisi["Ad"] == ad) and (kisi["Soyad"] == soyad):
            yeni_ad = input("Yeni bir isim giriniz: ")
            yeni_soyad = input("Yeni bir soyad giriniz: ")
            yeni_telno = input("Yeni bir tel no giriniz: ")

            kisi["Ad"] = yeni_ad
            kisi["Soyad"] = yeni_soyad
            kisi["Tel_No"] = yeni_telno
while True:
    print("""
        1.Kişi Ekle
        2.Kişi Sil
        3.Kişileri Listele
        4.Kişi Güncelleme
        5.Çıkış
        """)
    secim = int(input("Fonksiyon seçiniz: "))

    if secim == 1:
        girdi_ad = input("İsim Giriniz: ")
        girdi_soyad = input("Soyadı Giriniz: ")
        girdi_telno = input("Tel no giriniz: ")
        kisi_ekle(girdi_ad, girdi_soyad, girdi_telno)
    if secim == 2:
        girdi_ad = input("İsim Giriniz: ")
        girdi_soyad = input("Soyadı Giriniz: ")
        kisi_sil(girdi_ad,girdi_soyad)
    if secim == 3:
        kisi_listele()
    if secim == 4:
        girdi_ad = input("İsim Giriniz: ")
        girdi_soyad = input("Soyadı Giriniz: ")
        kisi_guncelle(girdi_ad,girdi_soyad)
    if secim == 5:
        break