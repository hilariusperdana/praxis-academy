#serialisasi
import pickle

#the object to serialize
example_dic={1:"6",2:"2",3:"f"}

#where the bytes after serializing end up at, wb stands for write byte
pickle_out=open("dict.pickle","wb")
#Time to dump
pickle.dump(example_dic,pickle_out)
#whatever you open, you must close
pickle_out.close()

#deserialisasi
import pickle

pickle_in=open("dict.pickle","rb")
get_deserialized_data_back=pickle.load(pickle_in)

print(get_deserialized_data_back)