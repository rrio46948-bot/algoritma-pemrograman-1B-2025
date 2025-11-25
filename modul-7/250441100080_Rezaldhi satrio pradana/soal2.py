inventaris = {}

def tambah_barang():
    print("\n--- TAMBAH BARANG ---")
    id_barang = input("Masukkan ID Barang: ").strip()

    if id_barang in inventaris:
        print(f"ID Barang '{id_barang}' sudah ada.")
        return

    nama = input("Nama Barang: ").strip().title()
    try:
        harga = float(input("Harga Satuan: "))
        stok = int(input("Stok Awal: "))
    except ValueError:
        print("Input harga/stok harus berupa angka.")
        return

    if harga < 0 or stok < 0:
        print("Harga dan Stok tidak boleh negatif.")
        return

    inventaris[id_barang] = [nama, harga, stok]
    print(f"Barang '{nama}' berhasil ditambahkan.")

def tampilkan_semua():
    print("\n--- DAFTAR INVENTARIS ---")
    if not inventaris:
        print("Gudang kosong.")
        return

    print(f"{'ID':<10}{'Nama Barang':<20}{'Harga':<10}{'Stok':<5}")
    for id_barang, data in inventaris.items():
        nama, harga, stok = data
        print(f"{id_barang:<10}{nama:<20}{harga:<10.0f}{stok:<5}")

def cari_barang():
    print("\n--- CARI BARANG ---")
    id_barang = input("Masukkan ID Barang: ").strip()

    if id_barang in inventaris:
        nama, harga, stok = inventaris[id_barang]
        print(f"\n[ Detail Barang ID: {id_barang} ]")
        print(f"Nama: {nama}")
        print(f"Harga: {harga:,.0f}")
        print(f"Stok: {stok}")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")

def perbarui_stok():
    print("\n--- PERBARUI STOK ---")
    id_barang = input("Masukkan ID Barang yang diubah: ").strip()

    if id_barang in inventaris:
        nama, harga, stok_lama = inventaris[id_barang]
        print(f"Stok saat ini untuk '{nama}' adalah: {stok_lama}")
        
        try:
            perubahan = int(input("Masukkan perubahan stok (+/-): "))
            stok_baru = stok_lama + perubahan

            if stok_baru < 0:
                print(f"Gagal: Stok tidak bisa menjadi negatif ({stok_baru}).")
                return

            inventaris[id_barang][2] = stok_baru
            print(f"Stok '{nama}' diperbarui menjadi {stok_baru}.")

        except:
            print("Input perubahan stok harus berupa bilangan bulat.")
        
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")

def hapus_barang():
    print("\n--- HAPUS BARANG ---")
    id_barang = input("Masukkan ID Barang yang dihapus: ").strip()

    if id_barang in inventaris:
        nama_dihapus = inventaris[id_barang][0]
        del inventaris[id_barang]
        print(f"Barang '{nama_dihapus}' (ID: {id_barang}) berhasil dihapus.")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")
def menu_utama():
    while True:
        print(" INVENTARIS GUDANG SEDERHANA")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang (ID)")
        print("3. Tambah Barang")
        print("4. Perbarui Stok")
        print("5. Hapus Barang")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ").strip()

        if pilihan == '1':
            tampilkan_semua()
        elif pilihan == '2':
            cari_barang()
        elif pilihan == '3':
            tambah_barang()
        elif pilihan == '4':
            perbarui_stok()
        elif pilihan == '5':
            hapus_barang()
        elif pilihan == '6':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_utama()