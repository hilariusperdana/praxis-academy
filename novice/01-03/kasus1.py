class home():
    def __init__(self,kategori,sambutan,produk_populer,informasi_lain):
        self.kategori = kategori
        self.sambutan = sambutan
        self.produk_populer = produk_populer
        self.informasi_lain = informasi_lain
        print('(kategori home : {})'.format(self.kategori))
    
    def tell(self):
        print('Nama: "{}" sambutan:"{}"'.format(self.kategori,self.sambutan), end=" ")

class kategori(home):
    def __init__(self,kategori,sambutan,no_telepon,kode_pos):
        home.__init__(self,kategori,sambutan,no_telepon,kode_pos)
        self.no_telepon = no_telepon
        self.kode_pos = kode_pos
        print('(kuliah di : {})'.format(self.kategori))
    
    def tell(self):
        home.tell(self)
        print('no telepon : "{}"'.format(self.no_telepon))
        print('Kode pos : "{}"'.format(self.kode_pos))

isi_home = home('kuliner','halo',21,'P')
isi_kategori = kategori('uad','jogja',12345,57662)

print()

total = [isi_home,isi_kategori]
for anggota in total:
    anggota.tell()