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
    
          
objek = []
print('Sebelum sort:',objek)
mergesort(objek)
print('Hasil sort:',objek)