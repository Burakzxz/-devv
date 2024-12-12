hak = 2  # Kullanıcı Yanlış Giriş Hak Değişkeni Ekliyoruz.
print("Uygulamamıza Hoş Geldiniz Lütfen Bilgilerinizi Giriniz: ")
ad = str(input("Adınızı Giriniz: "))
soyad = str(input("Soyadınızı Giriniz: "))
Username = str(input("Kullanıcı Adı Oluşturunuz: ")).lower()
# Şifre alırken kontrol
while True:
    try:
        sifre = int(input("Şifrenizi Oluşturunuz: "))  # Şifreyi string olarak alıyoruz
        print("Başarıyla Oluşturuldu", Username, "")
        break  # Şifre başarıyla alındığında döngüden çık
    except ValueError:
        print("Lütfen geçerli bir şifre giriniz.")
# Giriş yap
print("\nGiriş Yapmak İçin Bilgilerinizi Giriniz: ")
girissorgu = False  # Giriş durumunu kontrol etmek için bir değişken ekliyoruz.
while hak > 0:
    kullanici = str(input("Kullanıcı Adınızı Giriniz: ")).lower()
    sifre2 = int(input("Şifrenizi Giriniz: "))  # Şifreyi string olarak alıyoruz
    if kullanici == Username and sifre2 == sifre:
        print("Hoş Geldin", Username)
        girissorgu = True
        break
    else:
        hak -= 1
        if hak > 0:
            print("Kullanıcı adı veya şifre hatalı. Kalan hakkınız:", hak)
        else:
            print("Hesabınız askıya alındı. Lütfen admin ile iletişime geçiniz.")
            break
# Seçenekler
if girissorgu:
    while True:
        print("\n1: Şifre Değişme \n2: Kullanıcı Verilerini Gör \n3:Sayı Tahmin Etme Oyunu:")
        try:
            secenek = int(input("Seçeneklerden Birini Seçiniz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
            continue  # Hatalı girişte döngünün başına dön.

        if secenek == 2:
            print("Adınız:", ad)
            print("Soyadınız:", soyad)
            print("Kullanıcı Adınız:", Username)
            break
        elif secenek == 1:
            while True:
                degistirme = input("\nŞifre Değiştirmek İster misiniz? (Evet/Hayır): ").lower()
                if degistirme == 'evet':
                    yenisifre = input("Yeni Şifrenizi Giriniz: ")
                    sifre = yenisifre  # Yeni şifreyi atıyoruz.
                    print("Şifre başarıyla değiştirildi.")
                    break
                elif degistirme == 'hayır':
                    print("Hoşgeldiniz!")
                    break
                else:
                    print("\nLütfen Geçerli Bir Cevap Giriniz.")
                    continue
        elif  secenek == 3:
            import random
            #1 ile 100 arasında sayı seç.
            hedef_sayi =random.randint(1,100)
            print("\n1 ile 100 Arasında bir sayı tahmin edin")
            #Tahmin Sayısı Tutan Değişken.
            tahmin_sayisi = 0
            #oyun döngü vs.
            while True:
                #kullanıcan tahmin alma 
                try:                             
                    tahmin = int(input("Tahmininiz: "))
                except ValueError:
                    print("Lütfen Sayı Giriniz:")
                    continue                               
                tahmin_sayisi +=1
                #kullanıcı tahmin kontrol
                if tahmin < hedef_sayi:
                    print("Daha yüksek bir sayı deneyin")
                if tahmin > hedef_sayi:
                    print("Daha küçük bir sayı deneyin")
                if tahmin == hedef_sayi:
                    print("Tebrikler!",tahmin_sayisi,"Denemede doğru sayıyı buldunuz:",hedef_sayi)
                    #Tekrar oyun oynamak için soru.
                    tekrar_oynama = input("Tekrar Oynamak İstermisiniz?")
                    if tekrar_oynama == 'evet':
                     tahmin_sayisi = 0
                     hedef_sayi =random.randint(1,100)
                     continue 
                    else:
                     exit()                                                                           
        else:
            print("Geçersiz seçenek. Lütfen geçerli bir seçenek giriniz.")
            continue 
