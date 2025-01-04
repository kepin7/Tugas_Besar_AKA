from prettytable import PrettyTable
import random
import time
import matplotlib.pyplot as plt

# Fungsi untuk membuat dataset secara dinamis
def buat_dataset(ukuran):
    dataset = []
    ids = random.sample(range(1, ukuran * 2), ukuran)
    kota_asal = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Semarang"]
    kota_tujuan = ["Purwokerto", "Kroya", "Kutoarjo", "Kiaracondong", "Solobalapan"]
    for i in range(ukuran):
        dataset.append({
            "id": ids[i],
            "kota_asal": random.choice(kota_asal),
            "kota_tujuan": random.choice(kota_tujuan),
            "waktu_keberangkatan": f"{random.randint(0, 23)}:{random.randint(0, 59):02}",
        })
    return dataset

# Fungsi sequential search secara iteratif
def pencarian_sequential_iteratif(dataset, keyword):
    for jadwal in dataset:
        if keyword.lower() in jadwal["kota_asal"].lower() or keyword.lower() in jadwal["kota_tujuan"].lower():
            return jadwal
    return False

# Fungsi sequential search secara rekursif
def pencarian_sequential_rekursif(dataset, keyword, indeks=0):
    if indeks >= len(dataset):
        return False
    if keyword.lower() in dataset[indeks]["kota_asal"].lower() or keyword.lower() in dataset[indeks]["kota_tujuan"].lower():
        return dataset[indeks]
    return pencarian_sequential_rekursif(dataset, keyword, indeks + 1)

# Fungsi untuk mencari jadwal dengan algoritma iteratif
def cari_jadwal_iteratif(dataset, keyword):
    waktu_mulai = time.perf_counter()
    hasil = pencarian_sequential_iteratif(dataset, keyword)
    waktu_selesai = time.perf_counter()
    waktu_total = max(waktu_selesai - waktu_mulai, 1e-6)
    return hasil, waktu_total

# Fungsi untuk mencari jadwal dengan algoritma rekursif
def cari_jadwal_rekursif(dataset, keyword):
    waktu_mulai = time.perf_counter()
    hasil = pencarian_sequential_rekursif(dataset, keyword)
    waktu_selesai = time.perf_counter()
    waktu_total = max(waktu_selesai - waktu_mulai, 1e-6)
    return hasil, waktu_total

# Program utama untuk input ukuran dataset
if __name__ == "__main__":
    print("Analisis Kompleksitas Algoritma Sequential Search pada Jadwal Kereta Api")

    iteratif_times = []
    rekursif_times = []
    dataset_sizes = []

    while True:
        try:
            ukuran = int(input("Silahkan Masukkan ukuran dataset (note = input 0 untuk keluar): "))
            if ukuran == 0:
                print("Program berhenti. Thankyou, Have a Nice Day!")
                break
            if ukuran < 0:
                print("Ukuran dataset harus positif. Silakan coba lagi.")
                continue

            dataset_sizes.append(ukuran)
            dataset = buat_dataset(ukuran)
            keyword = input("Masukkan nama kota asal atau tujuan untuk pencarian: ")

            print(f"Mencari jadwal kereta api dengan kata kunci: {keyword}")

            hasil_iteratif, waktu_iteratif = cari_jadwal_iteratif(dataset, keyword)
            hasil_rekursif, waktu_rekursif = cari_jadwal_rekursif(dataset, keyword)

            if hasil_iteratif:
                print(f"Pencarian Iteratif: Jadwal kereta api ditemukan: {hasil_iteratif}, Waktu: {waktu_iteratif:.6f} detik")
            else:
                print(f"Pencarian Iteratif: Jadwal kereta api tidak ditemukan, Waktu: {waktu_iteratif:.6f} detik")

            if hasil_rekursif:
                print(f"Pencarian Rekursif: Jadwal kereta api ditemukan: {hasil_rekursif}, Waktu: {waktu_rekursif:.6f} detik")
            else:
                print(f"Pencarian Rekursif: Jadwal kereta api tidak ditemukan, Waktu: {waktu_rekursif:.6f} detik")

            iteratif_times.append(waktu_iteratif)
            rekursif_times.append(waktu_rekursif)

        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # Membuat tabel hasil analisis
    print("\nHasil Analisis Waktu:")
    tabel = PrettyTable()
    tabel.field_names = ["Ukuran Input", "Waktu Rekursif (d)", "Waktu Iteratif (d)"]
    for i, ukuran in enumerate(dataset_sizes):
        tabel.add_row([ukuran, f"{rekursif_times[i]:.6f}", f"{iteratif_times[i]:.6f}"])
    print(tabel)

    # Membuat grafik 
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
