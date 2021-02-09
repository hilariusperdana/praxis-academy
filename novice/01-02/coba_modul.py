#pilih salah satu

from m_insertionsort import InsertionSort
from m_bubblesort import BubbleSort
from m_mergesort import mergesort
from m_quicksort import QuickSort
from m_selesctionsort import selectionsort

#masukkan data dan jenis sorting
objek = ['data']
'jenis sorting'(objek)
print("hasil",objek)

#khusus quicksort format seperti berikut
objek = ['data']
QuickSort(objek,0,len(objek)-1)
print("hasil",objek)
