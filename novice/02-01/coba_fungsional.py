# def apply_duakali(func,arg):
#     return func(func(arg))
# def kali_lima(x):
#     return x+5
# print(apply_duakali(kali_lima,10))

#lambda


# hasil = (lambda x,y: x**2 + y**2)(4,6)
# print(hasil)

t=[1,2,3,4,5]
s=[3,9,8,7,7]
hasil = lambda x,y: (x*2) + (y*2)
hasil2=map(hasil,t,s)
print(list(hasil2))

t=[1,2,3,4,5]
s=[3,9,8,7,7]
hasil = map (lambda x,y: x**2 +y**2,t,s)
print(list(hasil))