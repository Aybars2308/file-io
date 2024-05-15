class Ogrenci:
    def __init__(self, ad, soyad, numara, sınıf):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.dersler = []
        self.sınıf = sınıf

    def bilgileri_goster(self):
        print("Adı:", self.ad)
        print("Soyadı:", self.soyad)
        print("Numarası:", self.numara)
        print("Aldığı Dersler:", self.dersler)
        print("Sınıfı:", self.sınıf)

    def ders_ekle(self, ders):
        print(f"{self.ad} {self.soyad} {ders} dersini aldı.")
        self.dersler.append(ders)

# Sınıftan bir örnek oluşturma
ogrenci1 = Ogrenci("Ahmet", "Yılmaz", 123456,7)

# Önce öğrenci bilgilerini gösterelim
ogrenci1.bilgileri_goster()

# Şimdi dersleri ekleyelim
ogrenci1.ders_ekle("Matematik")
ogrenci1.ders_ekle("Fizik")
