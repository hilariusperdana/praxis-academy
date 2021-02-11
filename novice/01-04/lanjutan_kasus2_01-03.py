#import math
# r=int(input('masukkan jari jari: '))
# print ('luas lingkaran',(math.pi*r**2))
#tambah
# def tambah(a,b):
#     return(a+b)

# hasil=tambah(1,2)
# print(hasil)
#rumus luas lingkaran
pi=22/7
def lcircle(pi,r):
    return[(pi)*(r**2)]

#rumus persegi
def square(s):
    return(s*s)

#rumus luas persegi panjang
def lrectangel(p,l):
    return(p*l)
    
#rumus luas segitiga
def ltriangle(a,t):
    return(a*t/2)

#rumus jajar genjang
def ljajargenjang(a,t):
    return(a*t)

# hasil1=square(2)
# hasil=lcircle(pi,7)
# print(hasil1)

#menu operasi
print('1.luas lingkaran')
print('2.luas persegi')
print('3.luas persegi panjang')
print('4.luas segitiga')
print('5.luas jajar genjang')

#pilih menu operasi
while True:
    
    pilih=input('silahkan pilih(1/2/3/4/5)')

    if pilih=='1':
        r=int(input('masukkan jari jari: '))
        print('hasil',lcircle(pi,r))
    elif pilih=='2':
        s=int(input('masukkan sisi: '))
        print('hasil',square(s))
    elif pilih=='3':
        p=int(input('masukkan panjang: '))
        l=int(input('masukkan lebar: '))
        print('hasil',lrectangel(p,l))
    elif pilih=='4':
        a=int(input('masukkan alas: '))
        t=int(input('masukkan tinggi: '))
        print('hasil',ltriangle(a,t))
    elif pilih=='5':
        a=int(input('masukkan alas: '))
        t=int(input('masukkan tinggi: '))
        print('hasil',ljajargenjang(a,t))
    else:
        print('pilihan tidak ada')

    #kembali ke awal

    kembali=input('ingin kembali kepilihan awal? (y/t) : ')
    if kembali=='y':
        continue
    elif kembali=='t':
        break
    else:
        break
