# Write a bot:

# 	bot functions:
		
# 		tarixi de => Indiki tariff qaytarmalidi
# 		ili de => Indiki ili qaytarmalidi
# 		Ayi de => Indiki Ayi qaytarmalidi
# 		saati de => Indiki saati qaytarmalidi
		
# 		"Flan" adli folder yarat => olduğumuz qovluqda verilen adla Folder yaratsın
# 		"Flan" adli folderi sil => olduğumuz qovluqda verilen adla Folderi silsin

# 		Hesabla (misal) => cavab


from datetime import datetime, date
import os
import sys
 
#  tarixlerin funksyalari basladi

now = datetime.now()
today = date.today()
time = now.strftime("%H:%M:%S")
ayy = datetime.now()
gun = datetime.now()


if (sys.argv[1] == "tarixi" and sys.argv[2] == "de"):
    print("Tarix:", today)
elif (sys.argv[1] == "ili" and sys.argv[2] == "de"):
    print("il:", today.year)
elif (sys.argv[1] == "ayi" and sys.argv[2] == "de"):
    print("Ay:", ayy.strftime("%B"))
elif (sys.argv[1] == "gunu" and sys.argv[2] == "de"):
    print("Gun:", ayy.strftime("%A"))
elif (sys.argv[1] == "saati" and sys.argv[2] == "de"):
    print("Saat:", time)


# tarixlerin funksyalari bitdi
# - - - - - - - - - - - - - - - - 

# qovluq funksyalari basladi

cwd = os.getcwd()
if (sys.argv[1] == "yeri" and sys.argv[2] == "goster"):
    print("Yeriniz:", cwd)



if (sys.argv[1] == "qovluq" and sys.argv[2] == "yarat"):
    directory = input("Qovluq adını qeyd et: ") 
    parent_dir = "/Users/hcyevelnur/Desktop/py/botpy/"
    path = os.path.join(parent_dir, directory) 
    os.mkdir(path)
    print(directory + ": adlı qovluqunuz yaradıldı.")
elif (sys.argv[1] == "qovluqu" and sys.argv[2] == "sil"):
    directory = input("Qovluq adını qeyd et: ") 
    parent_dir = "/Users/hcyevelnur/Desktop/py/botpy/"
    path = os.path.join(parent_dir, directory) 
    os.rmdir(path)
    print(directory + ": adlı qovluqunuz silindi.")

# qovluq funksyalari bitdi

# - - - - - - - - - - - - - - - - 

# cals funksyalari basladi

if sys.argv[1] =="+":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "+", Y, "=", X + Y)
elif sys.argv[1] == "-":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "-", Y, "=", X - Y)
elif sys.argv[1] == "*":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "*", Y, "=", X * Y)
elif sys.argv[1] == "/":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "/", Y,"=", X / Y)

# cals funksyalari bitdi

elif sys.argv[1] == "not" and sys.argv[2] == "yarat":
    try:
        f = open(input("Yaradılacaq not adını daxil et: "),"x")
        print("Not yaradıldı")
    except:
        print("Bu adlı note var!")
    

elif sys.argv[1] == "not" and sys.argv[2] == "update" and sys.argv[3] == "ele":
    f = open(input("Update edilən not adını daxil et: "), "a")
    f.write(input("not adı: "))
    print("Not dəyişdirildi")    

elif sys.argv[1] == "notu" and sys.argv[2] == "goster":
    file = open(input("Göstəriləcək not adını daxil et: "), "r")
    print("Not göstərildi")    
    content = file.read()
    print(content)
    file.close()

elif sys.argv[1] == "notu" and sys.argv[2] == "sil":
    try:
        name = input("Silinəcək not adını daxil et: ")
        os.remove(name)
        print(f"{name} Adli Not silindi!")
    except:
        print("Belə not yoxdur!")


elif sys.argv[1] == "notun" and sys.argv[2] == "yazisini" and sys.argv[3] == "sil":
    f = open(input("not adı: "), "r+")
    f.seek(0)
    f.truncate()
    print("Not yazısı silindi!")

if (sys.argv[1] == "salam"):
    print("Salam, necə kömək edə bilərəm?")
    
elif sys.argv[1] == "necesen":
    print("Mən süni intellektəm, duyğularım yoxdur. Sizə necə köməkçi edə bilərəm?")
    print("Siz necəsiniz?")

if (sys.argv[1] == "nomremi" and sys.argv[2] == "duzelt"):
    a = []
    a.append(input("Nömrəni qeyd et: "))

    def decor(fn):
        def inner(a):
            fn("+994" +" "+ c[1]+ c[2] +" " + c[3]+ c[4] + c[5]  +" "+c[6]+c[7] +" "+c[-2:] for c in a)
        return inner

    @decor
    def number(a):
        print(*a)

    number(a)

class tapaz:
    miqdari = "10 ədəd" 
    satilib = "40 ədəd"

    def __init__(self, name, tipi, ram, Prosessor, Yaddaş, color, kredit, videokart, kamerasi, battery, sale, ayliq):
        self.name = name
        self.tipi = tipi
        self.ram = ram
        self.Prosessor = Prosessor
        self.Yaddaş = Yaddaş
        self.color = color
        self.kredit = kredit
        self.videokart = videokart
        self.kamerasi = kamerasi
        self.battery = battery
        self.sale = sale
        self.ayliq = ayliq

    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("RAM: {}".format(self.ram))
        print("Prosessor: {}".format(self.Prosessor))
        print("Videokart: {}".format(self.videokart))
        print("Batarya: {}".format(self.battery))
        print("Ön kamera: {}".format(self.kamerasi))
        print(f"Kredit: {self.kredit}")
        print("Rəng: {}".format(self.color))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        # print("Endirim: {}".format(self.e))
        print(f"Qiymət: {self.sale} AZN")




    def get_info(self):
        print(f"Hazırda stokda {self.name} markalı komputer mövcuddur.")

    def get_sale(self):
        if self.sale == 12:
            print(self.sale//12)
        elif self.sale == 24:
            print(self.sale//24)
        elif self.sale == 18:
            print(self.sale//18)

    def get_sale (self):
        if self.sale > 500:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 200} AZN")

asus = tapaz("Asus", "Notebook","4 GB", 'Intel Core I5',"512 GB SSD", 'Qara','Var', '6 GB', '18 MP', "6500 mAh", 2400, 12)
apple = tapaz("Apple", "Macbook","8 GB", 'M1',"518 GB SSD", 'Gray','Var', '4 GB', '12 MP', "9500 mAh", 3620, 12)
lenevo = tapaz("Lenovo", "Notebook","8 GB", 'Intel Core I7',"500 GB SSD", 'Qara','Var', '6 GB', '16 MP', "6500 mAh", 1800, 12)
toshiba = tapaz("Toshiba", "Notebook","2 GB", 'Intel Core I3',"300 GB HDD", 'Qara','Var', '2 GB', '8 MP', "2500 mAh", 820, 12)
dell = tapaz("Dell", "Notebook","4 GB", 'Intel Core I3',"300 GB HDD", 'Ağ','Var', '2 GB', '8 MP', "3500 mAh", 800, 12)


if (sys.argv[1] == "Notebook" and sys.argv[2] == "al"): 
    # a = input("Seç- ")
    apple.salam()
    apple.get_sale()
    apple.get_info()

# --- --- --- notebook classi bitdi --- --- ---




# --- --- --- Telefon class basladi --- --- ---

class tapaz:
    miqdari = "3"
    satilib = "12"

    def __init__(self, name, tipi, ram, Prosessor, Yaddaş, color, kredit, kamerasi, battery, sale, ayliq):
        self.name = name
        self.tipi = tipi
        self.ram = ram
        self.Prosessor = Prosessor
        self.Yaddaş = Yaddaş
        self.color = color
        self.kredit = kredit
        self.kamerasi = kamerasi
        self.battery = battery
        self.sale = sale
        self.ayliq = ayliq


    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("RAM: {}".format(self.ram))
        print("Prosessor: {}".format(self.Prosessor))
        print("Batarya: {}".format(self.battery))
        print("Əsas kamera: {}".format(self.kamerasi))
        print(f"Kredit: {self.kredit}")
        print("Rəng: {}".format(self.color))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        print(f"Qiymət: {self.sale} AZN")


    def get_info(self):
        print(f"Hazırda stokda {self.name} adli telefon mövcuddur. ")

    def get_sale (self):
        if self.sale > 500:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 200} AZN")

iphone = tapaz("Apple", "İphone","8 GB", 'A16',"1 TB", 'Purple', 'Var', '45 MP', "4500 mAh", 2500, 12)
samsung = tapaz("Samsung", "S23","8 GB", 'Snapdragon 8 Gen',"1 TB", 'Ağ', 'Var', '50 MP + 10MP + 12 MP', "3900 mAh", 2139, 12)
xiaomi = tapaz("Xiaomi", "12 Lite","8 GB", 'Qualcomm',"128 TB", 'Qara', 'Var', '108 MP', "4300 mAh", 899, 12)
nokia = tapaz("Nokia", "G21","4 GB", 'Unisoc',"128 GB", 'Göy', 'Var', '50 MP', "5050 mAh", 429, 12)
huawei = tapaz("Huawei", "Nova Y70","4 GB", 'Kirin',"128 GB", 'Kristal Göy', 'Var', '48 MP', "6000 mAh", 399, 12)

if (sys.argv[1] == "Telefon" and sys.argv[2] == "al"): 
    huawei.salam()
    huawei.get_sale()
    huawei.get_info()

# --- --- --- Telefon class bitdi --- --- ---


# --- --- --- Saat ve televizor class basladi --- --- ---


class tapaz:
    miqdari = "25"
    satilib = "120"

    def __init__(self, name, tipi, color, kredit, battery, sale):
        self.name = name
        self.tipi = tipi
        self.color = color
        self.kredit = kredit
        self.battery = battery
        self.sale = sale

    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("Batarya: {}".format(self.battery))
        print("Kredit: {}".format(self.kredit))
        print("Rəng: {}".format(self.color))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        print(f"Qiyməti: {self.sale} AZN")

    def get_info(self):
        print(f"Hazırda stokda {self.name} {self.tipi} mövcuddur. ")

    def get_sale (self):
        if self.sale > 500:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 50} AZN")

apple = tapaz("Apple", "Watch Ultra",'Ağ', 'Var',"542 mAh", 2199)
xiaomi = tapaz("Xiaomi", "Redmi Watch 2 Lite",'Qara', 'Var',"262 mAh", 130)
huawei = tapaz("Huawei", "Watch FİT 16",'Ağ', 'Var',"180 mAh", 159)


samsung = tapaz("Samsung", "Smart TV LED",'Qara', 'Var',"Tutumu yoxdur", 899)
xiaomi = tapaz("Xiaomi", "Smart TV LED",'Ağ', 'Var',"Tutumu yoxdur", 699)
lg = tapaz("LG", "Smart TV LED",'Qara', 'Var',"Tutumu yoxdur", 249)


if (sys.argv[1] == "Saat" and sys.argv[2] == "al"):
    huawei.salam()
    huawei.get_sale()
    huawei.get_info()

if (sys.argv[1] == "Televizor" and sys.argv[2] == "al"):
    samsung.salam()
    samsung.get_sale()
    samsung.get_info()


# --- --- --- Saat ve televizor class bitdi --- --- ---


# --- --- --- Kamera class basladi --- --- ---


class tapaz:
    miqdari = "12"
    satilib = "105"

    def __init__(self, name, tipi, color, kredit, battery, kamerasi, sale):
        self.name = name
        self.tipi = tipi
        self.color = color
        self.kredit = kredit
        self.battery = battery
        self.kamerasi = kamerasi
        self.sale = sale


    def salam(self):
        print("Adı: {}".format(self.name))
        print("Növü: {}".format(self.tipi))
        print("Batarya: {}".format(self.battery))
        print("Kredit: {}".format(self.kredit))
        print("Rəng: {}".format(self.color))
        print("Kamera: {}".format(self.kamerasi))
        print("Miqdarı: {}".format(self.miqdari))
        print("Satilib: {}".format(self.satilib))
        print(f"Qiymət: {self.sale} AZN")


    def get_info(self):
        print(f"Hazırda stokda {self.name} {self.tipi} mövcuddur. ")

    def get_sale (self):
        if self.sale > 200:
            print(f"Nəğd alışda endirimli qiyməti: {self.sale - 109} AZN")

canon = tapaz("Canon", "EOS 850D",'Qara', 'Var',"890 mAh", "3840 x 2160 (4k UHD)", 1799)
sony = tapaz("Sony", "Alpha ILCE-7C",'Qara', 'Var',"994 mAh","3840 x 2160 (4k UHD)", 4499)
nikon = tapaz("Nikon", "D850 Body",'Qara', 'Var',"882 mAh","3840 x 2160 (4k UHD)", 6499)
leica = tapaz("Leica", "M10-R SL",'Qara', 'Var',"1290 mAh","7864 x 5200", 16739)



if (sys.argv[1] == "Kamera" and sys.argv[2] == "al"):
    sony.salam()
    sony.get_sale()
    sony.get_info()



# --- --- --- Kamera class bitdi --- --- ---


class elanqoyy:
    def __init__(self):
        self.salam = []

    def eylansaxla(self):
        name = input("Marka: ")
        tipi = input("Növü: ")
        batarya = input("Batarya: ")
        color = input("Rəngi: ")
        kamera = input("Əsas Kamerası: ")
        ram = input("RAM: ")
        yaddas = input("Yaddaşı: ")
        prosessor = input("Prasessor: ")
        qiymet = input("Qiyməti: ")
        try:
         with open(input("Yaradılacaq not adını daxil et: "),"x") as file:
            file.write(f"Markası: {name}\nNövü: {tipi}\nBataryası: {batarya}\nRəngi: {color}\nKamerası: {kamera}\nRAM: {ram}\nYaddaşı: {yaddas}\nPrasessor: {prosessor}\nQiyməti: {qiymet}\n------------------------\n")

            print("Not yaradıldı")
            elanqoy2 = {"marka": name, "növü": tipi, "batarya": batarya, "rəngi": color, "kamera": kamera, "ram": ram, "yaddas": yaddas, "prosessor": prosessor, "qiymeti": qiymet,}
            self.salam.append(elanqoy2)
            print("Elanınız saxlanıldı!")
        except:
            print("Bu adlı not var!")
            print("Not adı eyni olduğu üçün elanınız saxlanılmadı!")  

if (sys.argv[1] == "elan" and sys.argv[2] == "yarat"):
    elan = elanqoyy()
    elan.eylansaxla()
elif sys.argv[1] == "elan" and sys.argv[2] == "sil":
    try:
        name = input("Silinəcək not adını daxil et: ")
        os.remove(name)
        print(f"{name} Adli Not silindi!")
    except:
        print("Belə not yoxdur!")