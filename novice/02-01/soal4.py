#comparison data string

# kondisi=input('masukkan kondisi anda saat ini')
# if kondisi == 'sehat':
#     print('silahkan masuk')
# elif kondisi != 'sehat':
#     print('tidak boleh masuk')
# else:
#     print('input salah')

#comparison data boolean
# x = 7
# y = 10
 
# print('x =',x)
# print('y =',y)
# print('\n')
 
# print('x == y hasilnya',x==y)
# print('x != y hasilnya',x!=y)
# print('x > y  hasilnya',x>y)
# print('x < y  hasilnya',x<y)
# print('x >= y hasilnya',x>=y)
# print('x <= y hasilnya',x<=y)

#comparison data integer

# umur=int(input('masukkan umur anda saat ini'))
# if umur >= 17:
#     print('punya KTP')
# elif umur < 17:
#     print('belum ada KTP')
# else:
#     print('input salah')

# latihan 2
# kondisi=input('masukkan kondisi anda saat ini')
# umur=input('masukkan umur anda')
# if (kondisi == 'sehat') and (umur>='17'):
#     print('silahkan masuk')
# elif ((kondisi != 'sehat') and (umur<'17'))
#     print('tidak boleh masuk')
# else:
#     print('input salah')

# print('[1] smartphone')
# print('[2] Hp jadul')
# jenis_hp=input('masukkan jenis handphone anda: ')
# tahun=int(input('masukkan tahun hp anda: '))
# if (jenis_hp=='1')or(tahun>=2017):
#     print('kirim chat WA')
# elif (jenis_hp=='2')or(tahun<2017):
#     print('kirim sms')
# else:
#     print('input salah')

#not
# print('Hasil dari not True  :', not True)
# print('Hasil dari not False :', not False)

#latihan 3

namaruangan=input('masukkan nama ruangan anda: ')
luasruangan=int(input('masukkan luas ruangan anda: '))
if (namaruangan=='kamar')and(luasruangan>=12):
    print('Besar')
elif (namaruangan=='kamar')and(luasruangan>6):
    print('sedang')
elif (namaruangan=='kamar')and(luasruangan<=6):
    print('kecil')
else:
    print('input salah')