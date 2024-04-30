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
yas_entry.grid(row=0,column=1,padx=5,pady=5)

pencere.mainloop()