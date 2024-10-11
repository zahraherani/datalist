# membuat list kosong (string)
list_buah =['lengkeng','apel','jambu','duren']
print(list_buah)
#angka kosong untuk menggantikann nama buah
angka = ['1','2','3'] 
print(angka)
#index nilai array = antrian nama menggunakan angka
print(list_buah[0])
print(list_buah[1])
print(list_buah[2])
print(list_buah[3])
# (-) untuk membalikkan data
print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])
print(list_buah[-4:-2])
print(list_buah[0:-1])
#ubah data menggunakan angka nama buah
list_buah[0]= 'naga'
print(list_buah)
#menambahkan data = insert(depan), input, append(belakang)
list_buah.append('melon')
print(list_buah)
list_buah.insert(3,'sawo')
print(list_buah)
#menghapus item dari list menggunakan pop
list_buah.pop(5)
print(list_buah)
#hapus menggunakan remove
list_buah.remove('sawo')
print(list_buah)
#del untuk menghapus spesifik index
del list_buah[0]
print (list_buah)
#clear menghapus semua item di list
#mengurutkan data
list_buah.sort()
print(list_buah)