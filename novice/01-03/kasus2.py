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
#rumus luas segitiga
#rumus jajar genjang

# hasil1=square(2)
# hasil=lcircle(pi,7)
# print(hasil1)

#menu operasi
print('1.luas lingkaran')
print('2.luas persegi')

#pilih menu operasi
pilih=input('silahkan pilih(1/2)')
x=int(input('masukkan angka pertama: '))
if pilih=='1':
    print('hasil',lcircle(pi,x))
elif pilih=='2':
    print('hasil',square(x))
else:
    print('pilihan tidak ada')
