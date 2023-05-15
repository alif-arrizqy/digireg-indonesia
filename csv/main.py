# 1. Skenario: Pengolahan Data CSV
# 2. Deskripsi: Anda memiliki file CSV yang berisi data transaksi penjualan. Anda diminta untuk membuat skrip Python yang membaca file CSV tersebut dan melakukan pengolahan sederhana pada data.
# Tugas:
# * Buatlah skrip Python yang membaca file CSV dan menyimpannya dalam bentuk struktur data yang sesuai.
#     * Lakukan pengolahan data berikut:
#     * Hitung total penjualan (jumlah kolom 'jumlah') dari semua transaksi.
#     * Temukan transaksi dengan nilai penjualan tertinggi (mencari baris dengan jumlah penjualan terbesar).
#     * Hitung jumlah transaksi (jumlah baris) dalam file CSV.
#     * Temukan dan cetak daftar produk yang terjual (isi kolom 'produk')
# 3. Kriteria penilaian:
# * Skrip Python harus dapat membaca file CSV dengan benar dan menyimpan data dalam struktur data yang sesuai.
# * Pengolahan data harus menghasilkan hasil yang akurat sesuai dengan deskripsi tugas.
# * Kode harus bersih, terstruktur, dan mengikuti praktik terbaik dalam pemrograman Python.

import csv


def produk():
    with open('produk.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_reader:
            csv_list.append(row)
        return csv_list


def total_penjualan():
    total = 0
    for row in produk():
        total += int(row['jumlah'])
    return total


def penjualan_tertinggi():
    penjualan = 0
    for row in produk():
        if int(row['jumlah']) > penjualan:
            penjualan = int(row['jumlah'])
    return penjualan


def jumlah_transaksi():
    return len(produk())


if __name__ == '__main__':
    total_penjualan = total_penjualan()
    penjualan_tertinggi = penjualan_tertinggi()
    jumlah_transaksi = jumlah_transaksi()
    print(f'Total penjualan: {total_penjualan}')
    print(f'Penjualan tertinggi: {penjualan_tertinggi}')
    print(f'Jumlah transaksi: {jumlah_transaksi}')