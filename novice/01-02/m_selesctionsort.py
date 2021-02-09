def selectionsort(objek):
    for pos_1 in range(len(objek)-1,0,-1):
        pos_max = 0
        for x in range(1,pos_1+1):
            max_sementara = objek[pos_max]
            if max_sementara < objek[x]:
                pos_max = x
        objek[pos_max],objek[pos_1] = objek[pos_1],objek[pos_max]

objek = []
selectionsort (objek)
print ("hasil",objek)
