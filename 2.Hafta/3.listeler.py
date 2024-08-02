#listeler içerisinde başka veri tiplerini de toplu bir şekilde bir arada tutabilen veri tipleridir
isim_listesi = ["Hasan","Hüseyin","Ali","Veli"]

print(isim_listesi)

#listeler içierisindeki verilere index'ine bakarak ulaşabiliriz.

#  [ veri_1,  veri_2,  veri_3 ]
#   0.index  1.index   2.index

liste_icindeki_ilk_veri = isim_listesi[0]
print(liste_icindeki_ilk_veri)

#listeleri for döngüsü ile beraber çok efektif bir şekilde kullanabiliriz

#Örnek
for isim in ["Ayşe", "Fatma", "Zeliha"]:
    print(isim)

#len() fonksiyonu listedeki elemanların tam sayısını bulmamıza yarar

meyveler = ["Elma", "Armut", "Portakal"]
print(len(meyveler))

#python içerisinde boş listeler tanımlayabiliriz
bos_liste = []
print(bos_liste)

#append() metodu bir listeye veri eklememizi sağlar.
bos_liste.append("Artık bu bir boş liste değil")
print(bos_liste)

#örnek
sayi_liste = []
for sayi in range(10):
    sayi_liste.append(sayi)

#yukarıdaki örneğin içerisine print fonksiyonu koyarak adım adım inceleyebilriiz
yeni_liste = []
for sayi in range(10):
    yeni_liste.append(sayi)
    print(yeni_liste)

#len() ve range() fonksiyonlarını bir arada kullanarak for döngüsü içerisinde indexler ile işlem yapabiliriz
#yukarıda tanımladığımız isim_listesi listesiyle bir örnek:

for index_no in range(len(isim_listesi)):
    print(isim_listesi[index_no], "çok güzel bir isimdir.")
