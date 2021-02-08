def shellsort (arr):
    n = len(arr)//2
    while n > 0:
        for mulai in range(n):
            gapInsertionSort(arr,mulai,n)
        print("setelah",n,"listnya",arr)
        n = n // 2
def gapInsertionSort(arr,start,gapP:
    for i in range(start+gap,len(arr),gap):
        value = arr[i]
        position = i
        while position >= gap and arr[position-gap]>value:
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position] = value
arr = [54,26,93,17,77,31,44,55,20]
shellsort(arr)
print(arr)