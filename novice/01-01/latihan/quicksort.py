def QuickSort(A,mulai,akhir):
    if mulai<akhir:
        pindex=partition(A,mulai,akhir)
        QuickSort(A,mulai,pindex-1)
        QuickSort(A,pindex+1,akhir)

def partition(A,mulai,akhir):
    pivot = A[akhir]
    pindex = mulai
    for i in range(mulai,akhir):
        if (A[i] <= pivot):
            A[i],A[pindex]=A[pindex],A[i]
            pindex += 1
    A[pindex],A[akhir] = A[akhir],A[pindex]
    return pindex

A = [54,26,93,17,77,31,44,55,20]
QuickSort(A,0,len(A)-1)
print(A)