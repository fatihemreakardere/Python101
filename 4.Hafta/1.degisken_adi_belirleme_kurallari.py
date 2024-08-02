#Değişken adları bir sayı ile başlayamaz. Yani şu kullanım yanlıştır:
3_kilo_elma = "5 TL"

#Değişken adları aritmetik işleçlerle başlayamaz. Yani şu kullanım yanlıştır:
+değer = 4568

#Değişken adları ya bir alfabe harfiyle ya da _ işaretiyle başlamalıdır:
_değer = 4568
değer = 4568

########
#Değişken isimlerinde türkçe karakter kullanaılabilir. Fakat beklenmedik durumlarlar karşılaşmamak için bundan kaçınılmalıdır.
########

#Aşağıdaki listedeki kelimeleri değişken olarak kullanamazsınız. Çünkü bu kelimeler python içerisinde zaten özel anlam içeren kelimelerdir.
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']