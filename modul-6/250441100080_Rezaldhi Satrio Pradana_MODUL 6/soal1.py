data_kunjungan = []
id_counter = 1
def tambah():
    global id_counter
    print("\n--- Tambah Pengunjung ---")
    nama_p = input("Nama Pengunjung: ")
    nama_s = input("Nama Santri: ")
    while True:
        asal = input("Daerah (Sumatra/Kalimantan/Jawa):").strip().capitalize()
        if asal in ["Sumatra", "Kalimantan", "Jawa"]: 
            break
        print("Daerah tidak valid. Harap masukkan 'Sumatra','Kalimantan', atau 'Jawa'.")
    data_kunjungan.append([id_counter, nama_p, nama_s, asal])
    print(f"Ditambahkan! ID Antrian: {id_counter}")
    id_counter += 1
def tampilkan():
    if not data_kunjungan:
        print("\nBelum ada data.")
        return

    print("\n## Daftar Pengunjung (Sumatra | Kalimantan | Jawa)")
    print("-" * 65)
    print(f"{'ID':<4} | {'Pengunjung':<20} | {'Santri':<20} |{'Daerah':<10}")
    for daerah in ["Sumatra", "Kalimantan", "Jawa"]:
        for id_antri, p, s, a in data_kunjungan:
            if a == daerah:
                print(f"{id_antri:<4} | {p:<20} | {s:<20} |{a:<10}")
    print("-" * 65)
def hapus():
    if not data_kunjungan: return print("\nData kosong.")
    id_hapus = int(input("\nMasukkan ID Antrian yang akan dihapus:"))
    indeks_ditemukan = -1
    for i in range(len(data_kunjungan)):
        if data_kunjungan[i][0] == id_hapus:
            indeks_ditemukan = i
            break

    if indeks_ditemukan != -1:
        data_dihapus = data_kunjungan.pop(indeks_ditemukan)
        print(f"ID {id_hapus} ({data_dihapus[1]}) berhasil dihapus.")
    else:
        print(f"ID Antrian **{id_hapus}** tidak ditemukan.")
def main():
        while True:
            print("\n=== Kunjungan Santri ===")
            print("1. Tambah")
            print("2. Tampilkan")
            print("3. Hapus")
            print("4. Keluar")
            pilihan = input("Pilih (1-4): ")
            if pilihan == '1': tambah()
            elif pilihan == '2': tampilkan()
            elif pilihan == '3': hapus()
            elif pilihan == '4':
                print("Sampai jumpa!")
                break

            else: print("Pilihan tidak valid.")
if __name__ == "__main__":
        main()
