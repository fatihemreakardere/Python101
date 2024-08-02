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