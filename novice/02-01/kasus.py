# const arr1 = [1, 2, 3];const arr2 = arr1.map(item => item * 2);console.log(arr2);

angka=[1,2,3,4,5,6,7,8,9,10]
min_satu=map(lambda x:x-1,angka)
print(list(min_satu))

flt=filter(lambda x:x-1,range(4,8))
print(list(flt))

from functools import reduce
angka2=[7,3,5,6]
rdc=reduce(lambda x: x - 1,angka2)
print(list(rdc))
#lanjuuuutt
