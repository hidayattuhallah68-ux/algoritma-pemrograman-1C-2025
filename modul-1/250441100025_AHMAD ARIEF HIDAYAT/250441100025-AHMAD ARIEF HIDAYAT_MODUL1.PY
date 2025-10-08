# TUGAS PRATIKUM

# 1. Menghitung total belanja setelah pajak
print("=== Soal 1: Hitung Total Belanja Setelah Pajak ===")
harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2

# Hitung total belanja sebelum pajak
total_sebelum_pajak = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

# Pajak 10%
pajak = 0.10 * total_sebelum_pajak

# Total setelah pajak
total_setelah_pajak = total_sebelum_pajak + pajak

print("Total belanja sebelum pajak: Rp", total_sebelum_pajak)
print("Pajak (10%): Rp", pajak)
print("Total belanja setelah pajak: Rp", total_setelah_pajak)


# 2. Menghitung volume dan luas permukaan balok
print("=== Soal 2: Hitung Volume dan Luas Permukaan Balok ===")

# Input dari user
panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

# Volume
volume = panjang * lebar * tinggi

# Luas permukaan = 2(pl + pt + lt)
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

print("Volume balok =", volume, "cm³")
print("Luas permukaan balok =", luas_permukaan, "cm²")


# 3. Menghitung kombinasi bola
print("=== Soal 3: Menghitung Kombinasi Bola ===")

# Membuat fungsi faktorial 
def faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    return hasil

# Jumlah kombinasi
n = 14   # total keseluruhan bola(8 bola biru + 6 bola merah)
r = 3    # bola yang diambil secara acak

# Rumus kombinasi: C(n, r) = n! / (r! * (n-r)!)
kombinasi = faktorial(14) / (faktorial(3) * faktorial(14 - 3))

print("Jumlah kombinasi bola yang dapat diambil:", int(kombinasi))