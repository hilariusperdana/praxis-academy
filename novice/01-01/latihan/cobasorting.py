def selectionsort(angka):
    for pos_1 in range(len(angka)-1,0,-1):
        pos_max = 0
        for x in range(1,pos_1+1):
            max_sementara = angka[pos_max]
            if max_sementara < angka[x]:
                pos_max = x
        angka[pos_max],angka[pos_1] = angka[pos_1],angka[pos_max]

angka = [34,21,45,32,12,31,19,23,54,31,25,27]
print (angka)
selectionsort (angka)
print (angka)
