#split() metodu bir stringi belirli bir karakter dizisiyle bölmek için kullanılır. Bölünen string bir liste içerisine konulur.

#Örnek 1
alınacaklar = "elma,armut,karpuz,patlıcan"
#print(alınacaklar)
#alınacaklar_liste = alınacaklar.split(",")
#print(alınacaklar_liste)
#
##Örnek2
# "Türkiye Büyük Millet Meclisi" stringinden "TBMM" çıktısını alalım
isim = "Türkiye Büyük Millet Meclisi"
#
##Yöntem 1 (sep, print fonksiyonunun bir parametresidir şu anlık görmezden gelinebilir.)
#print(isim[0], isim[8], isim[14], isim[21], sep="") #Herbir harfin indexini teker teker yazarak sonuca ulaşıyoruz.

##Yöntem 2 (end, print fonksiyonunun bir parametresidir şu anlık görmezden gelinebilir.)
#isim = "Türkiye Büyük Millet Meclisi"
#isim_liste = isim.split(" ") #Önce herbir kelimeyi bir liste içerisine koyuyoruz
#print(isim_liste)
#for kelime in isim_liste: #Daha sonrasında döngü ile her bir kelimenin ilk harfine ulaşarak çıktı alıyoruz.
#    print(kelime[0], end="")

##Deneme
#Bu denemede öğrenciler değişkenindeki isimleri çıktı olarak alalım.
#split() metodu ile böldüğümüzde yalnızca isimleri elde
#ettiğimizden emin olalım!!!
ogrenciler = "Ahmet, Mehmet, Kezban, Mualla, Süreyya, Veli"