X = [3,4,6,7,5,9,6,2,1,0,3,8,9,4,7,6,1,3,7,8]

user = int(input("Masukkan angka dalam rentang 0-10 : "))

jumlah = X.count(user)
indeks = []

if jumlah > 0:  
    if user % 2 == 0:  
        for i in range(len(X)):
            if X[i] == user:
                indeks.append(i)
        print("Jumlah munculnya angka", user, "adalah", jumlah)
        print("Indeks angka", user, "adalah", indeks)
    else:
        print("Tidak ada hasil karena angka tersebut ganjil.")
else:
    print("Tidak ada hasil karena angka tidak ditemukan di list.")
