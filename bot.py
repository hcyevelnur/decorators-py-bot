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
    print("Il:", today.year)
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
    f = open(input("Yaradılacaq not adını daxil et: "),"x")
    print("Not yaradıldı")

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
    os.remove(input("Silinəcək not adını daxil et: "))
    print("Not silindi!")

elif sys.argv[1] == "notun" and sys.argv[2] == "yazisini" and sys.argv[3] == "sil":
    f = open(input("not adı: "), "r+")
    f.seek(0)
    f.truncate()

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
