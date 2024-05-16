# import os
# import csv
# import tkinter
# import customtkinter
# import tkinter as tk
# from tkinter import ttk  # Treeview widget için
# from tkinter import messagebox

# customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         # configure window
#         self.title("Human Record")
#         self.geometry(f"{1200}x{700}")

#         # configure grid layout (4x4)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure((2, 3), weight=0)
#         self.grid_rowconfigure((0, 1, 2), weight=1)   


#                 #  sidebar frame  widgets
#         self.sidebar_frame = customtkinter.CTkFrame(self, width=160, corner_radius=0)
#         self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
#         self.sidebar_frame.grid_rowconfigure(4, weight=1)
#         self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="MediaMarkt", font=customtkinter.CTkFont(size=40, weight="bold", slant="italic"))
#         self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.sidebar_Ekle = customtkinter.CTkButton(self.sidebar_frame, text="Ekle",command="")
#         self.sidebar_Ekle.grid(row=1, column=0, padx=20, pady=10)
#         self.sidebar_Düzenle = customtkinter.CTkButton(self.sidebar_frame,text="Düzenle", command="")
#         self.sidebar_Düzenle.grid(row=2, column=0, padx=20, pady=10)
#         self.sidebar_Sil = customtkinter.CTkButton(self.sidebar_frame,text="Sil(Çoklu silme)", command="")
#         self.sidebar_Sil.grid(row=3, column=0, padx=20, pady=10)        
#         self.sidebar_Yenile = customtkinter.CTkButton(self.sidebar_frame,text="Yenile", command="")
#         self.sidebar_Yenile.grid(row=4, column=0, padx=20, pady=10)





#         # create treeview
#         self.style = ttk.Style()
#         self.style.configure("Treeview", font=("Proxima Nova", 10), rowheight=40, relief="solid")
#         self.inventory_treeview = ttk.Treeview(self, columns=("Ad Soyad", "Kimlik No", "Yaş", "Doğum Tarihi",  "Memleket", "Medeni hal"), show="headings", style="Treeview",padding=20)
#         self.inventory_treeview.heading("Ad Soyad", text="Ad Soyad", anchor="w")
#         self.inventory_treeview.heading("Kimlik No", text="Kimlik No", anchor="w")
#         self.inventory_treeview.heading("Yaş", text="Yaş", anchor="w")
#         self.inventory_treeview.heading("Doğum Tarihi", text="Doğum Tarihi", anchor="w")
#         self.inventory_treeview.heading("Memleket", text="Memleket", anchor="w")
#         self.inventory_treeview.heading("Medeni hal", text="Medeni hal", anchor="w")

#         self.inventory_treeview.column("Ad Soyad", width=150, anchor="w")  # İlk sütun için genişlik ve hizalama ayarlandı
#         self.inventory_treeview.column("Kimlik No", width=50, anchor="w")
#         self.inventory_treeview.column("Yaş", width=50, anchor="w")
#         self.inventory_treeview.column("Doğum Tarihi", width=20, anchor="w")
#         self.inventory_treeview.column("Memleket", width=30, anchor="w")
#         self.inventory_treeview.column("Medeni hal", width=30, anchor="w")
#         self.inventory_treeview.grid(column=0, row=0, sticky="s")
#         self.inventory_treeview.columnconfigure(0, weight=1)

#         self.inventory_treeview.grid(row=0, column=1,  padx=(0, 0), pady=(0, 0), sticky="nsew")
        
#         vsb = ttk.Scrollbar(self, orient="vertical", command=self.inventory_treeview.yview)
#         vsb.grid(row=0, column=2, sticky='ns')
#         self.inventory_treeview.configure(yscrollcommand=vsb.set)
#         # self.reload_inventory()

#     def add_item(self):
#         self.new_frame = customtkinter.CTkFrame(self)
#         self.new_frame.grid(row=0, column=3, padx=(10, 20), pady=(10, 0), sticky="nsew")
#         self.logo_label = customtkinter.CTkLabel(self.new_frame, text="EKLE", font=customtkinter.CTkFont(size=20, weight="bold"))
#         self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))





# if __name__ == "__main__":
#     app = App()
#     app.mainloop()



import os
import csv
import tkinter
import customtkinter
import tkinter as tk
from tkinter import ttk  # Treeview widget için
from tkinter import messagebox

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.inventory_list=[]

        # configure window
        self.title("Human Record")
        self.geometry(f"{1200}x{700}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)   

        # sidebar frame widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="MediaMarkt", font=customtkinter.CTkFont(size=40, weight="bold", slant="italic"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_Ekle = customtkinter.CTkButton(self.sidebar_frame, text="Ekle", command=self.add_people)
        self.sidebar_Ekle.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_Düzenle = customtkinter.CTkButton(self.sidebar_frame, text="Düzenle", command=self.edit_record)
        self.sidebar_Düzenle.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_Sil = customtkinter.CTkButton(self.sidebar_frame, text="Sil(Çoklu silme)", command=self.delete_record)
        self.sidebar_Sil.grid(row=3, column=0, padx=20, pady=10)        
        self.sidebar_Yenile = customtkinter.CTkButton(self.sidebar_frame, text="Yenile", command=self.reload_records)
        self.sidebar_Yenile.grid(row=4, column=0, padx=20, pady=10)

        # create treeview
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Proxima Nova", 10), rowheight=40, relief="solid")
        self.inventory_treeview = ttk.Treeview(self, columns=("Ad Soyad", "Kimlik No", "Yaş", "Doğum Tarihi",  "Memleket", "Medeni hal"), show="headings", style="Treeview",padding=20)
        self.inventory_treeview.heading("Ad Soyad", text="Ad Soyad", anchor="w")
        self.inventory_treeview.heading("Kimlik No", text="Kimlik No", anchor="w")
        self.inventory_treeview.heading("Yaş", text="Yaş", anchor="w")
        self.inventory_treeview.heading("Doğum Tarihi", text="Doğum Tarihi", anchor="w")
        self.inventory_treeview.heading("Memleket", text="Memleket", anchor="w")
        self.inventory_treeview.heading("Medeni hal", text="Medeni hal", anchor="w")

        self.inventory_treeview.column("Ad Soyad", width=150, anchor="w")  # İlk sütun için genişlik ve hizalama ayarlandı
        self.inventory_treeview.column("Kimlik No", width=50, anchor="w")
        self.inventory_treeview.column("Yaş", width=50, anchor="w")
        self.inventory_treeview.column("Doğum Tarihi", width=20, anchor="w")
        self.inventory_treeview.column("Memleket", width=30, anchor="w")
        self.inventory_treeview.column("Medeni hal", width=30, anchor="w")
        self.inventory_treeview.grid(column=0, row=0, sticky="s")
        self.inventory_treeview.columnconfigure(0, weight=1)

        self.inventory_treeview.grid(row=0, column=1,  padx=(0, 0), pady=(0, 0), sticky="nsew")

    def add_people(self):
        self.new_frame = customtkinter.CTkFrame(self)
        self.new_frame.grid(row=0, column=3, padx=(10, 20), pady=(10, 0), sticky="nsew")
        self.logo_label = customtkinter.CTkLabel(self.new_frame, text="EKLE", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.entry1lbl = customtkinter.CTkLabel(master=self.new_frame,text="Ad Soyad:"  )
        self.entry1lbl.grid(row=1, column=0, pady=(10, 0), padx=5, sticky="n")
        self.entry1 = customtkinter.CTkEntry(master=self.new_frame)
        self.entry1.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="n")
        self.entry2lbl = customtkinter.CTkLabel(master=self.new_frame,text="Kimlik NO:"  )
        self.entry2lbl.grid(row=2, column=0, pady=(10, 0), padx=10, sticky="n")
        self.entry2 = customtkinter.CTkEntry(master=self.new_frame)
        self.entry2.grid(row=2, column=1, pady=(10, 0), padx=10, sticky="n")
        self.entry3lbl = customtkinter.CTkLabel(master=self.new_frame,text="Yaş:")
        self.entry3lbl.grid(row=3, column=0, pady=(10, 0), padx=10, sticky="n")
        self.entry3 = customtkinter.CTkEntry(master=self.new_frame)
        self.entry3.grid(row=3, column=1, pady=(10, 0), padx=10, sticky="n")
        self.label4 = customtkinter.CTkLabel(master=self.new_frame, text="Doğum Tarihi:")
        self.label4.grid(row=4, column=0, padx=5, pady=(10, 0),sticky="n")
        self.entry4 = customtkinter.CTkEntry(master=self.new_frame, validate="key", validatecommand=(self.new_frame.register(self.validate_integer_input), "%P"))
        self.entry4.grid(row=4, column=1, pady=(10, 0), padx=5, sticky="n")
  
        self.appearance_mode_label = customtkinter.CTkLabel(master=self.new_frame, text="Memleket:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(20, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=self.new_frame ,values=["SDT", "TAMGÖR", "ORTAKLIK"])
        self.appearance_mode_optionemenu.grid(row=5, column=1, padx=20, pady=(20, 10))
        self.appearance_mode_label1 = customtkinter.CTkLabel(master=self.new_frame, text="Medeni Hal:", anchor="w")
        self.appearance_mode_label1.grid(row=6, column=0, padx=20, pady=(20, 0))
        self.appearance_mode_optionemenu1 = customtkinter.CTkOptionMenu(master=self.new_frame ,values=["Bebek(0-5)", "Çocuk/Ergen(5-12-18)", "Reşit(18+)"])
        self.appearance_mode_optionemenu1.grid(row=6, column=1, padx=20, pady=(20, 10))
        
        self.add_buton=customtkinter.CTkButton(master=self.new_frame, text="Tamam",command=self.apply ,width=50)
        self.add_buton.grid(row=7, column=0, padx=20, pady=(20, 0))

    def validate_integer_input(self, P):
        if P == "" or P.isdigit():
            return True
        else:
            return False


    def apply(self):
                new_ad_soyad = self.entry1.get()
                new_kimlik_no = self.entry2.get()
                new_yas = self.entry3.get()
                new_dogum_tarihi = self.entry4.get()
                new_memleket = self.appearance_mode_optionemenu.get()
                new_medeni_hal = self.appearance_mode_optionemenu1.get()

                if new_ad_soyad and new_kimlik_no and new_yas and new_memleket and new_dogum_tarihi:
                    with open('inventory.csv', 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow([new_ad_soyad, new_kimlik_no, new_yas,new_dogum_tarihi,new_memleket , new_medeni_hal])
                    self.clear_entries()
                    messagebox.showinfo("Başarılı", "Kişi başarıyla envantere eklendi!")
                    self.reload_inventory()
                else:
                    messagebox.showerror("Hata", "Tüm alanların doldurulması zorunludur!")

        
                vsb = ttk.Scrollbar(self, orient="vertical", command=self.inventory_treeview.yview)
                vsb.grid(row=0, column=2, sticky='ns')
                self.inventory_treeview.configure(yscrollcommand=vsb.set)
                self.reload_records()

    def clear_entries(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')

    def reload_inventory(self):
        # Clear the inventory_list to avoid duplicates
        self.inventory_list.clear()

        self.inventory_treeview.delete(*self.inventory_treeview.get_children())

        file_name = 'kayitlar.csv'

        # Check if the file exists, and create it if it doesn't
        if not os.path.exists(file_name):
            open(file_name, 'w').close()

        with open(file_name, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                self.inventory_treeview.insert('', 'end', values=row, iid=f'I{i}')
                self.inventory_list.append(list(row))

    def edit_record(self):
        self.selected_index = self.inventory_treeview.selection()

        if not self.selected_index:
            messagebox.showerror("Hata", "Düzenlecek öğe seçiniz!")
            return

        self.selected_index = self.inventory_treeview.selection()[0]
        self.item_data = self.inventory_list[int(self.selected_index.lstrip('I'))]

        self.new_frame = customtkinter.CTkFrame(self)
        self.new_frame.grid(row=0, column=3, padx=(10, 20), pady=(10, 0), sticky="nsew")
        self.logo_label = customtkinter.CTkLabel(self.new_frame, text="EKLE", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.entry1lbl = customtkinter.CTkLabel(master=self.new_frame,text="Ad soyad:"  )
        self.entry1lbl.grid(row=1, column=0, pady=(10, 0), padx=5, sticky="n")
        self.entry1 = customtkinter.CTkEntry(master=self.new_frame)
        self.entry1.grid(row=1, column=1, pady=(10, 0), padx=10, sticky="n")
        self.entry1.insert(0, self.item_data[0] if self.item_data[0] is not None else "")

        self.entry2lbl = customtkinter.CTkLabel(master=self.new_frame,text="Kimlik NO:"  )
        self.entry2lbl.grid(row=2, column=0, pady=(10, 0), padx=10, sticky="n")
        self.entry2 = customtkinter.CTkEntry(master=self.new_frame)
        self.entry2.grid(row=2, column=1, pady=(10, 0), padx=10, sticky="n")
        self.entry2.insert(0, self.item_data[1] if self.item_data[1] is not None else "")


        self.entry3lbl = customtkinter.CTkLabel(master=self.new_frame,text="Yaş:")
        self.entry3lbl.grid(row=3, column=0, pady=(10, 0), padx=10, sticky="n")
        self.entry3 = customtkinter.CTkEntry(master=self.new_frame)
        self.entry3.grid(row=3, column=1, pady=(10, 0), padx=10, sticky="n")
        self.entry3.insert(0, self.item_data[2] if self.item_data[2] is not None else "")

 
        self.label4 = customtkinter.CTkLabel(master=self.new_frame, text="Doğum Tarihi:")
        self.label4.grid(row=4, column=0, padx=5, pady=(10, 0),sticky="n")
        self.entry4 = customtkinter.CTkEntry(master=self.new_frame, validate="key", validatecommand=(self.new_frame.register(self.validate_integer_input), "%P"))
        self.entry4.grid(row=4, column=1, pady=(10, 0), padx=5, sticky="n")
        self.entry4.insert(0, self.item_data[3] if self.item_data[3] is not None else "")

  
        self.appearance_mode_label = customtkinter.CTkLabel(master=self.new_frame, text="Memleket:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(20, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=self.new_frame ,values=["SDT", "TAMGÖR", "ORTAKLIK"])
        self.appearance_mode_optionemenu.grid(row=5, column=1, padx=20, pady=(20, 10))
        self.appearance_mode_optionemenu.set(self.item_data[4] if self.item_data[4] is not None else "")


        self.appearance_mode_label1 = customtkinter.CTkLabel(master=self.new_frame, text="Medeni Hal:", anchor="w")
        self.appearance_mode_label1.grid(row=6, column=0, padx=20, pady=(20, 0))
        self.appearance_mode_optionemenu1 = customtkinter.CTkOptionMenu(master=self.new_frame ,values=["Yeni", "Kullanılmış", "Arızalı"])
        self.appearance_mode_optionemenu1.grid(row=6, column=1, padx=20, pady=(20, 10))
        self.appearance_mode_optionemenu1.set(self.item_data[5] if self.item_data[5] is not None else "")
        
        self.add_buton=customtkinter.CTkButton(master=self.new_frame, text="Tamam",command=self.editapply ,width=50)
        self.add_buton.grid(row=7, column=0, padx=20, pady=(20, 0))

    def editapply(self):
        new_ad_soyad = self.entry1.get()
        new_kimlik_no = self.entry2.get()
        new_yas = self.entry3.get()
        new_memleket = self.entry4.get()
        new_dogum_tarihi = self.appearance_mode_optionemenu.get()
        new_medeni_hal = self.appearance_mode_optionemenu1.get()

        if new_ad_soyad and new_kimlik_no and new_yas and new_dogum_tarihi:
            self.item_data[0] = new_ad_soyad
            self.item_data[1] = new_kimlik_no
            self.item_data[2] = new_yas
            self.item_data[3] = new_memleket
            self.item_data[4] = new_dogum_tarihi
            self.item_data[5] = new_medeni_hal
            self.inventory_treeview.item(self.selected_index, values=self.item_data)
            with open('inventory.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for item in self.inventory_list:
                    writer.writerow(item)
            self.result = True
            messagebox.showinfo("Başarılı", "Öğe başarıyla düzenlendi!")
        else:
            messagebox.showerror("Hata", "Tüm alanların doldurulması zorunludur!")

    def delete_item(self):
        selected_indices = self.inventory_treeview.selection()
        if not selected_indices:
            messagebox.showerror("Hata", "Lütfen silinecek öğe/öğeleri seçiniz!")
            return

        # Seçilen indeksleri öğe numaralarına dönüştürme
        oge_nolar = [int(selected_index.lstrip('I')) for selected_index in selected_indices]

        # Dizin çakışmalarını önlemek için seçili öğeleri ters sırayla silme
        for oge_no in sorted(oge_nolar, reverse=True):
            self.selected_index = f'I{oge_no}'
            self.inventory_treeview.delete(self.selected_index)
            self.inventory_list.pop(oge_no)

        with open('inventory.csv', 'w', newline='', encoding="UTF-8") as file:
            writer = csv.writer(file)
            for item in self.inventory_list:
                writer.writerow(item)

        messagebox.showinfo("Başarılı", "Öğe/Öğeler başarıyla silindi.")

    def search_item(self):
        search_query = self.entry_ara.get().strip().lower()

        self.inventory_treeview.delete(*self.inventory_treeview.get_children())  # Mevcut sonuçları temizle

        if not search_query:
            # Boş arama kutusu, sonuçları temizle
            self.reload_inventory()
        
        # Arama sorgusuyla sadece belirli sütunlarda ve seçilen şirketlere göre eşleşen öğeleri göster
        for i, item_data in enumerate(self.inventory_list):

            product_description = item_data[0].strip().lower()
            serial_number = item_data[1].strip().lower()
            part_number = item_data[2].strip().lower()
            company = item_data[4].strip().lower()

            if (
                (
                    (self.check1_var.get() == "on" and "Anne" in company) or
                    (self.check2_var.get() == "on" and "Baba" in company) or
                    (self.check3_var.get() == "on" and "Akrabalar" in company)
                )
                or
                (search_query in product_description or
                search_query in serial_number or
                search_query in part_number)
            ):

                item_index = f'I{i}'
                self.inventory_treeview.insert('', 'end', values=item_data, iid=item_index)

    def reload_records(self):
        self.inventory_treeview.delete(*self.inventory_treeview.get_children())
        with open('kayitlar.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.inventory_treeview.insert('', 'end', values=row)

    def add_record(self):
        # Burada bir kayıt eklemek için gerekli işlemleri yapabilirsiniz
        pass

    def edit_record(self):
        # Burada bir kaydı düzenlemek için gerekli işlemleri yapabilirsiniz
        pass

    def delete_record(self):
        # Burada bir veya birden fazla kaydı silmek için gerekli işlemleri yapabilirsiniz
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
