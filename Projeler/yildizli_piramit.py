#Bu örneğimizde düzgün bir piramit yazdırmak için öncelikle her satırdaki boşluklarımızı belirliyoruz

#Her adımda i sayısı artacağından ve boşluğun azalmasını istediğimizden " " karakterini (10-i) ile çarpıyoruz

#"*" karakterini 1,3,5,7... gibi tek sayılar şeklinde istediğimizden "*" karakterini tek sayı formülü olan (2*i-1) ile çarpıyoruz

for i in range(10):
    print(" " * (10-i) + "*" * (2*i-1))