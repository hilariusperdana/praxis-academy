print('welcome to the simple ATM')
print('  ')
print('please select ATM transaction')
print('press [1] Deposit')
print('press [2] Withdraw')
print('press [3] Balance Inquiry')
print('press [4] Exit')

#pilihan
while True:
    pilih=input('What would you like to do? ')
    if pilih=='1':
        masukkansaldo=int(input('silahkan masukkan jumlah yang ingin anda masukkan: '))
        print('anda ingin deposit senilai',masukkansaldo)
        pilihandeposit=input('apakah jumlah yang anda masukkan sudah benar? [y/t]: ')
        if pilihandeposit=='y':
            print('selamat saldo anda bertambah',masukkansaldo)
            pilihanmenulain=input('anda ingin melakukan transaksi lainnya?[y/t]')
            if pilihanmenulain=='y':
                continue 
            elif pilihanmenulain=='t':
                break
            else:
                break
        if pilihandeposit=='t':
            print('setoran anda di batalkan')
            pilihanmenulain=input('anda ingin melakukan transaksi lainnya?[y/t]')
            if pilihanmenulain=='y':
                continue
            elif pilihanmenulain=='t':
                break
            else:
                break

    elif pilih=='2':
        keluarkansaldo=int(input('silahkan masukkan jumlah yang ingin anda ambil: '))
        print('anda ingin mengambil',keluarkansaldo,'?')
        pilihankeluar=input('apakah jumlah yang ingin anda ambil sudah benar? [y/t]: ')
        if pilihankeluar=='y':
            print('silahkan ambil uang anda')
            pilihanmenulain=input('anda ingin melakukan transaksi lainnya?[y/t]')
            if pilihanmenulain=='y':
                continue 
            elif pilihanmenulain=='t':
                break
            else:
                break
        if pilihankeluar=='t':
            print('pengambilan anda di batalkan')
            pilihanmenulain=input('anda ingin melakukan transaksi lainnya?[y/t]')
            if pilihanmenulain=='y':
                continue
            elif pilihanmenulain=='t':
                break
            else:
                break
          
    elif pilih=='3':
        print('saldo anda','xxx')
        pilihanmenulain=input('anda ingin melakukan transaksi lainnya?[y/t]')
        if pilihanmenulain=='y':
            continue
        elif pilihanmenulain=='t':
            break
        else:
            break
    elif pilih=='4':
        print('anda yakin ingin meninggalkan kami?')
        pilihanexit=input('[y/t]')
        if pilihanexit=='y':
            print('terima kasih sudah menggunakan jasa kami')
            break
        if pilihanexit=='t':
            print('ingin transaksi lainnya')
        
    else:
        print('perintah yang anda masukkan salah')
        break