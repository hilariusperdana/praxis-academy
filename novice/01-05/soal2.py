#soal no 1
jarak=range(3,15)
print('jarak dari rumah hingga sekolah adalah',len(jarak),'km')

#soal no 2
kalimat = "Corona cepat selesai"
print(kalimat.upper())
print(kalimat.count('e'))

#soal no 3
obj_list = [11.25, 18.0, 20.0, 10.75, 9.50]
def mean_list(inp_list):
    inp_list=obj_list
    return(sum(inp_list)/len(inp_list))

print(mean_list(obj_list))

#soal no 4
obj_list = [2, 4, 5, 6]
obj_penambah = [1, 2, 3]

def kali_list(x,y):
    x=obj_list
    y=obj_penambah
    return(x+y)
 
print(kali_list(obj_list, obj_penambah))

