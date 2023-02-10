# Dekoratorlar vasitesi ile yazilacaq:
	
# 	input vasitesi ile dcxil olunan mobil nomreleri seliqeye salan program.

# 	example:

# 	input:	0552781026
	
# 	output: +994 55 278 10 26



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