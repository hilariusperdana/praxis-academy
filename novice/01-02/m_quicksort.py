def QuickSort(objek,mulai,akhir):
    if mulai<akhir:
        pindex=partition(objek,mulai,akhir)
        QuickSort(objek,mulai,pindex-1)
        QuickSort(objek,pindex+1,akhir)

def partition(objek,mulai,akhir):
    pivot = objek[akhir]
    pindex = mulai
    for i in range(mulai,akhir):
        if (objek[i] <= pivot):
            objek[i],objek[pindex]=objek[pindex],objek[i]
            pindex += 1
    objek[pindex],objek[akhir] = objek[akhir],objek[pindex]
    return pindex

objek = []
QuickSort(objek,0,len(objek)-1)
print("hasil",objek)