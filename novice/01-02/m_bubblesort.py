def BubbleSort(objek):
    n = len(objek)
    for i in range(n-1): 
        for j in range(0, n-i-1):
            if objek[j] > objek[j+1] :
                objek[j], objek[j+1] = objek[j+1], objek[j]

objek = []
BubbleSort(objek)
print("hasil",objek)
    