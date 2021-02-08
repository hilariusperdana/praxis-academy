def InsertionSort(objek):
    for x in range(1,len(objek)):
        objekaktif = objek[x]
        posisi = x
        while posisi>0 and objek[posisi-1]>objekaktif:
            objek[posisi]=objek[posisi-1]
            posisi = posisi-1
        objek[posisi]=objekaktif
objek = [23,7,32,99,4,15,11,20]
InsertionSort(objek)
print(objek)