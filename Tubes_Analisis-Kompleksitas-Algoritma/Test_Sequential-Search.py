import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi untuk membuat dataset dinamis
def buat_dataset(size):
    return [
        {
            "id": i,
            "kota_asal": f"Kota {chr(65 + (i % 26))}",
            "kota_tujuan": f"Kota {chr(90 - (i % 26))}",
            "waktu_keberangkatan": f"{i % 24:02}:00",
        }
        for i in range(1, size + 1)
    ]

# Fungsi sequential search (Iteratif)
def sequential_search_iteratif(data, keyword):
    for jadwal in data:
        if keyword.lower() in jadwal["kota_asal"].lower():
            return jadwal
    return False

# Fungsi sequential search (Rekursif)
def sequential_search_rekursif(data, keyword, index=0):
    if index >= len(data):
        return False
    if keyword.lower() in data[index]["kota_asal"].lower():
        return data[index]
    return sequential_search_rekursif(data, keyword, index + 1)

# Fungsi untuk mencari jadwal berdasarkan algoritma iteratif & rekursif
def cari_jadwal(data, keyword):
    # Pencarian menggunakan iteratif
    waktu_mulai = time.perf_counter()
    hasil_iteratif = sequential_search_iteratif(data, keyword)
    waktu_selesai = time.perf_counter()
    waktu_iteratif = waktu_selesai - waktu_mulai

    # Pencarian menggunakan rekursif
    waktu_mulai = time.perf_counter()
    hasil_rekursif = sequential_search_rekursif(data, keyword)
    waktu_selesai = time.perf_counter()
    waktu_rekursif = waktu_selesai - waktu_mulai

    # Menampilkan hasil
    if hasil_iteratif:
        print(f"\nPencarian Iteratif: \nJadwal kereta api ditemukan: {hasil_iteratif}, Waktu: {waktu_iteratif:.6f} detik")
    else:
        print(f"Pencarian Iteratif: \nJadwal kereta api tidak ditemukan, Waktu: {waktu_iteratif:.6f} detik")

    if hasil_rekursif:
        print(f"Pencarian Rekursif: \nJadwal kereta api ditemukan: {hasil_rekursif}, Waktu: {waktu_rekursif:.6f} detik")
    else:
        print(f"Pencarian Rekursif: \nJadwal kereta api tidak ditemukan, Waktu: {waktu_rekursif:.6f} detik")

    return waktu_iteratif, waktu_rekursif

def main():
    print("Hai!. Selamat datang di pencarian jadwal kereta api!")

    iteratif_times = []
    rekursif_times = []
    dataset_sizes = []

    while True:
        try:
            size = int(input("Silahkan Masukkan ukuran dataset (note = input 0 untuk keluar): "))
            if size == 0:
                print("Program berhenti. Terima kasih sudah menggunakan. Berikut hasil analisis waktu dan grafik perbandingannya:")
                break
            if size < 0:
                print("Ukuran dataset tidak boleh negatif. Silakan coba lagi.")
                continue

            dataset_sizes.append(size)
            data_jadwal = buat_dataset(size)
            waktu_iteratif, waktu_rekursif = cari_jadwal(data_jadwal, "Kota A")
            iteratif_times.append(waktu_iteratif)
            rekursif_times.append(waktu_rekursif)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # Menampilkan tabel analisis waktu
    print("\nHasil Analisis Waktu:")
    tabel = PrettyTable()
    tabel.field_names = ["Ukuran Input", "Waktu Iteratif (d)", "Waktu Rekursif (d)"]
    for i, ukuran in enumerate(dataset_sizes):
        tabel.add_row([ukuran, f"{iteratif_times[i]:.6f}", f"{rekursif_times[i]:.6f}"])
    print(tabel)

    # Membuat grafik jika ada data yang diinputkan
    if dataset_sizes:
        plt.figure(figsize=(10, 6))
        plt.plot(dataset_sizes, iteratif_times, label='Iteratif', marker='o', color='black', linestyle='-', linewidth=2)
        plt.plot(dataset_sizes, rekursif_times, label='Rekursif', marker='o', color='green', linestyle='-', linewidth=2)
        plt.xlabel('Ukuran Dataset', fontsize=12)
        plt.ylabel('Waktu (detik)', fontsize=12)
        plt.title('Perbandingan Waktu Pencarian Iteratif vs Rekursif pada Jadwal Kereta Api', fontsize=14)
        plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.ylim(0, max(max(iteratif_times), max(rekursif_times)) * 1.2)
        plt.legend(
            fontsize=10,
            loc='upper center',
            bbox_to_anchor=(0.5, 1.15),
            fancybox=True,
            shadow=True,
            ncol=2
        )
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
