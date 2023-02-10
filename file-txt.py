# Notes application:

# Not yaradan bot application yazilmalidi.

# Funksiyanalliqlar:
	
# 	1. Note yarad
# 	2. Note lari goster
# 	3 . Notu sil
# 	4. Notu update ele


import sys
import os


if sys.argv[1] == "not" and sys.argv[2] == "yarat":
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
