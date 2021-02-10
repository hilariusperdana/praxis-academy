pilihan = input("silahkan pilih(1/2/3/4/5): ")
x = int(input("masukkan angka pertama: "))
y = int(input("masukkan angka kedua: "))
if pilihan == '1':
    print("hasil",x+y)
elif pilihan == '2':
    print("hasil",x-y)
elif pilihan == '3':
    print("hasil",x*y)
elif pilihan == '4':
    print("hasil",x/y)
elif pilihan == '5':
    print("hasil",x**y)
else :
    print("pilihan tidak ada")