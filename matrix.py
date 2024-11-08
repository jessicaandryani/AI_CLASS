# Jessica Andryani F55123051


# menggunakan library Numpy
import numpy as np

# Definisikan matriks A, B, dan C
A = np.array([[2, 0, -3],
              [1, 4, 5]])

B = np.array([[3, 1],
              [-1, 0],
              [4, 2]])

C = np.array([[4, 7],
              [2, 1],
              [1, -1]])

# Hitung A*B dan A*C
AB = np.dot(A, B)
AC = np.dot(A, C)

# Hitung AB + AC
hasil = AB + AC

print("Hasil AB:\n", AB)
print("Hasil AC:\n", AC)
print("Hasil AB + AC:\n", hasil)


# tidak menggunakan Library numpy

A = [[2, 0, -3],
     [1, 4, 5]]

B = [[3, 1],
     [-1, 0],
     [4, 2]]

C = [[4, 7],
     [2, 1],
     [1, -1]]

# perlurangan mengalikan matriks
def kalikan_matriks(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

# perulangan menjumlahkan matriks
def jumlahkan_matriks(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]


AB = kalikan_matriks(A, B)
AC = kalikan_matriks(A, C)


hasil = jumlahkan_matriks(AB, AC)

# Cetak hasil
print("Hasil AB:")
for baris in AB:
    print(baris)

print("\nHasil AC:")
for baris in AC:
    print(baris)

print("\nHasil AB + AC:")
for baris in hasil:
    print(baris)
