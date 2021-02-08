def mergesort(objek):
  if len(objek) > 1:
    tengah = len(objek)//2
    kiri = objek[:tengah]
    kanan = objek[tengah:]
    
    mergesort(kiri)
    mergesort(kanan)

  
    all,kr,kn = 0,0,0 
    
    while kr < len(kiri) or kn < len(kanan):
      if kr == len(kiri): 
        objek[all] = kanan[kn]
        kn = kn + 1
      elif kn == len(kanan): 
        objek[all] = kiri[kr]
        kr = kr + 1
      elif kiri[kr] <= kanan[kn]: 
        objek[all] = kiri[kr]
        kr = kr + 1
      else: 
        objek[all] = kanan[kn]
        kn = kn + 1
      all = all + 1
    
          
angka = [6,5,3,1,8,7,2,4]
print('Sebelum sort:',angka)
mergesort(angka)
print('Setelah sort:',angka)