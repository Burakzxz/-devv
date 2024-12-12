# Bu Kütüphane tarih işlemleri yapmak için kullanılır
from datetime import date

#Türkçe günler için kütüphane eklentisi
import locale

# Locale Ayarını Türkçe Yapıyoruz
locale.setlocale(locale.LC_TIME, "tr_TR.utf8")

# Bugünün tarihini alıyoruz
bugunun_tarihi = date.today()
#Bu  fonksiyon kullanıcıdan tarih değerlerini alır (yıl, ay veya gün)
def tarih_girdisi_al(metin, min_deger, max_deger):
    #Kullanıcıdan belirli bir aralıkta geçerli tarih girdisi almak için yardımcı fonksiyon oluştıuruyoz
    while True:
        try:
            deger = int(input(metin))
            if not (min_deger <= deger <= max_deger):
                print("Lütfen",min_deger,"ile",max_deger,"arasında bir değer giriniz.")
            else:
                return deger
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

# Kullanıcıdan Gerekli Bilgileri Alıyoruz
dogum_yili = tarih_girdisi_al("\nDoğum yılınızı girin: ", 1900, bugunun_tarihi.year)
dogum_ayi = tarih_girdisi_al("\nDoğum ayınızı girin (1-12): ", 1, 12)
dogum_gunu = tarih_girdisi_al("\nDoğum gününüzü girin (1-31): ", 1, 31)

# Geçerli bir tarih oluşturmayı deneriz
while True:
    try:
        dogum_tarihi = date(dogum_yili, dogum_ayi, dogum_gunu)
        break
    except ValueError:
        print("Geçersiz bir tarih girdiniz.")
        continue
    

# Yaşı hesapla
#Kullanıcının yaşı, bugünkü yıl ile doğum yılı arasındaki fark alınarak hesaplanır
#Eğer bugünün ay ve günü, doğum tarihinin ay ve gününden küçükse yaş bir azaltılır

yas = bugunun_tarihi.year - dogum_tarihi.year
if (bugunun_tarihi.month, bugunun_tarihi.day) < (dogum_tarihi.month, dogum_tarihi.day):
    yas -= 1

# Gün farkını hesapla
son_dogum_gunu = date(
    bugunun_tarihi.year if (bugunun_tarihi.month, bugunun_tarihi.day) >= (dogum_tarihi.month, dogum_tarihi.day)
    else bugunun_tarihi.year - 1,
    dogum_ayi, dogum_gunu)
gecen_gun_sayisi = (bugunun_tarihi - son_dogum_gunu).days

# Bir sonraki doğum günü
if (bugunun_tarihi.month, bugunun_tarihi.day) < (dogum_tarihi.month, dogum_tarihi.day):
    bir_sonraki_dogum_gunu = date(
        bugunun_tarihi.year, dogum_ayi, dogum_gunu)
else:
    bir_sonraki_dogum_gunu = date(
        bugunun_tarihi.year + 1, dogum_ayi, dogum_gunu)

# Gün ismini alıyoruz (örnek: Pazartesi)
#strftime fonksiyonu ile bir sonraki doğum gününün hangi güne denk geldiği belirliyo
bir_sonraki_gun_adi = bir_sonraki_dogum_gunu.strftime("%A")

# Sonuçları Yazdırma
print("Yaşınız:",yas,"yıl ve",gecen_gun_sayisi,"gün.")
print(f"Bir sonraki doğum gününüz: {bir_sonraki_dogum_gunu} - {bir_sonraki_gun_adi}")
#70 Satır Görünsün Diye :)