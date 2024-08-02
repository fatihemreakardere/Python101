# İsim, Boy ve Kilo Bilgilerini Alma
isim = input("İsim: ")
boy = float(input("Boyunuz (cm): "))
kilo = float(input("Kilonuz (kg): "))

# Vücut Kitle Endeksi (BMI) Hesaplama
bmi = kilo / ((boy / 100) ** 2)

# BMI Sonucunu Değerlendirme
if bmi < 18.5:
    durum = "Zayıf"
elif 18.5 <= bmi < 24.9:
    durum = "Normal"
elif 25 <= bmi < 29.9:
    durum = "Fazla Kilolu"
else:
    durum = "Obez"

# Sonuçları Yazdırma
print("Merhaba " + isim  + ". Vücut Kitle Endeksiniz " + str(bmi) + ". " + durum + " kilo aralığındasın.")