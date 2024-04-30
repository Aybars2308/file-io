import tkinter as tk
from tkinter import messagebox

def kayit_ekle(ad,yas,d_tarihi,dosya_yolu):
    try:
        with open(dosya_yolu,"a") as dosya:
            dosya.write(f"Ad:{ad},Yaş: {yas},Doğum tarihi {d_tarihi}\n")
        print("Kayit başarıyla tamamlandı") 
    except IOError:
        print("Dosyaya yazdırma hatası!")


def kayitlari_göster(dosya_yolu):
    try:
        with open(dosya_yolu,"r") as dosya:
            print("---------Kayıtlar---------")
            for satir in dosya:
                print(satir, end="")
    except FileNotFoundError:
        print("Kayıt Dosyası Bulunamadı")


def kayit_sil(ad_soyad, dosya_yolu):
    try:
        with open(dosya_yolu, 'r') as dosya: # kullanacağımız dosyayı okuma modunda aç
            satirlar = dosya.readlines() # bütün satırları oku ve satirlar değişkenşne ata
        with open(dosya_yolu, 'w') as dosya: #dosyayı yazama modunda aç
            silindi = False
            for satir in satirlar: # kaydedilen satırlar arasında dolaş
                if ad_soyad not in satir: # eğer istenilen ad soyad mevcut olamayan bir satıra denk gelinirse
                    dosya.write(satir) # dosyanın boş olan satrını yazınız.
                else:
                    silindi=True
            if silindi:
                print(f"{ad_soyad} adlı kişinin kaydı başarıyla silindi!")
            else:
                print(f"hata")
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı")



dosya_yolu = "kayitlar.txt"

pencere =tk.Tk()
pencere.title("Kayıt Tutma programı")

# Ad Soyad giriş etiketi ve entrysi
ad_label = tk.Label(pencere,text="Ad Soyad")
ad_label.grid(row=0,column=0,padx=5,pady=5)
ad_entry=tk.Entry(pencere)
ad_entry.grid(row=0,column=1,padx=5,pady=5)

# Yaş giriş etiketi ve entrysi
yas_label = tk.Label(pencere,text="Yaş")
yas_label.grid(row=1,column=0,padx=5,pady=5)
yas_entry=tk.Entry(pencere)
yas_entry.grid(row=1,column=1,padx=5,pady=5)

# Yaş giriş etiketi ve entrysi
yas_label = tk.Label(pencere,text="Doğum TArihi")
yas_label.grid(row=2,column=0,padx=5,pady=5)
yas_entry=tk.Entry(pencere)
yas_entry.grid(row=2,column=1,padx=5,pady=5)

#kayıt ekleme butonu
ekle_buton = tk.Button(pencere,text="EKLE",command=kayit_ekle)
ekle_buton.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

pencere.mainloop()