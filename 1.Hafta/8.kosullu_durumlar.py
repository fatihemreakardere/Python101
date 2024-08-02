#if ifadesi belirtilen durumların doğruluklarını kontrol eder.

yas = 15
if yas > 13:
    print("Filmi izleyebilirsiniz")


#elif ifadesi eğer değilse manasına gelir gibi düşünebiliriz. if koşulunu sağlamayan durumlarda kontrol edilir.

yas = 12

if yas >= 13:
    print("Filmi izleyebilirsiniz.")
elif yas < 13:
    print("Filmi izlemek için çok küçüksünüz.")

#else ifadesi koşullu önermede hiçbir durumun gerçekleşmemesi durumunda çalışır.

yas = -7

if yas >= 13:
    print("Filmi izleyebilirsiniz.")
elif yas > 0 and  yas < 13:
    print("Filmi izlemek için çok küçüksünüz.")
else:
    print("Heyyy! Yaşın bu olamaz...")