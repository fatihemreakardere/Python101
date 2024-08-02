#Bu örnekte basit bir Adam Asmaca oyununu yapalım.

hata_hakkı = 5
dogru_cevap = input("Gizli kelimeyi giriniz: ")
dogru_cevap_liste = list(dogru_cevap)
kullanıcı_cevabı = ["_"] * len(dogru_cevap_liste)
while hata_hakkı > 0:
    kullanıcı_girdisi = input("Bir harf giriniz: ")
    if kullanıcı_girdisi in dogru_cevap_liste:
        for i in range(len(dogru_cevap_liste)):
            if kullanıcı_girdisi == dogru_cevap_liste[i]:
                kullanıcı_cevabı[i] = kullanıcı_girdisi
        print(kullanıcı_cevabı)
        if kullanıcı_cevabı == dogru_cevap_liste:
            print("Doğru cevabı buldunuz!!! Oyun Bitti...")
            break
    else:
        #hata_hakkı = hata_hakkı -1
        hata_hakkı -= 1
        print("Yanlış Bildiniz. Kalan hata hakkı:", hata_hakkı)
        if hata_hakkı == 0:
            print("Hata Hakkınız kalmadı yıkıksın...")
