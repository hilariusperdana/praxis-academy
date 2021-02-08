def BubbleSort(objek):
    n = len(objek)
    for i in range(n-1): 
        for j in range(0, n-i-1):
            if objek[j] > objek[j+1] :
                objek[j], objek[j+1] = objek[j+1], objek[j]

objek = [34,21,45,32,12,31,19,23,54,31,25,27]
BubbleSort(objek)
print("hasil",objek)
    