# ad,soyad
# yas
# dogum tarihi


def kayit_ekle(ad_soyad,yas,dogum_tarihi,dosya_yolu):
    try:
        with open(dosya_yolu,'a') as dosya:
           dosya.write(f"Ad Soyad: {ad_soyad}, Yaş: {yas}, Doğum Tarihi: {dogum_tarihi}\n")
        print("Kayıt başarıyla tamamlandı!")
    except IOError:
        print("Dosyaya yazdırma hatası!")


def kayitlari_goster(dosya_yolu):
    try:
        with open(dosya_yolu,'r') as dosya:
             print("----------Kayıtlar----------")
             for satir in dosya:
                 print(satir,end='')
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı")


def kayit_sil(ad_soyad, dosya_yolu):
    try:
        with open(dosya_yolu, 'r') as dosya:
            satirlar = dosya.readlines()
        with open(dosya_yolu, 'w') as dosya:
            for satir in satirlar:
                if ad_soyad not in satir:
                    dosya.write(satir)
        print(f"{ad_soyad} adlı kişinin kaydı başarıyla silindi!")
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı")
                 


dosya_yolu = "kayitlar.txt"



while True:
    print("""
          1.Yeni Kayıt Ekle          
          2.Kayıtları Göster
          3.Kayıt Sil
          4.Çıkış
    """)
    
    secim = input("Yapmak istediğiniz işlemin numarasını giriniz:")

    if secim =="1":
        ad_soyad = input("Ad Soyad girin: ")
        yas = input("Yaşınızı girin: ")
        dogum_tarihi = input("Dogum tarihinizi girin: ")
        kayit_ekle(ad_soyad,yas,dogum_tarihi,dosya_yolu)

    elif secim =="2":
        kayitlari_goster(dosya_yolu)

    

    elif secim == "3":
        ad_soyad = input("Silmek istediğiniz kişinin adını ve soyadını girin: ")
        kayit_sil(ad_soyad, dosya_yolu)

    elif secim =="4":
        print("programdan çıkılıyor")
        break
    else:
        print("Geçersiz seçim! Lütfen Tekrar deneniyiz")
