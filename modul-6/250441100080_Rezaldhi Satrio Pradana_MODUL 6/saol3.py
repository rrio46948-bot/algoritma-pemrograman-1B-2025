# List global untuk menyimpan semua angka yang diinput
data = []
# Fungsi untuk menambah angka
def tambah():
# Mengambil input angka dan menyimpannya sebagai integer

    angka = int(input("Masukkan angka: "))
    # Menambahkan angka ke akhir list 'data'
    data.append(angka)
# Fungsi untuk menampilkan seluruh list
def tampilkan():
    print("Data:", data)
# Fungsi untuk mengubah angka berdasarkan indeks
def ubah_angka():
    indeks = int(input("Masukkan indeks yang ingin diubah: "))
    # Pengecekan: Memastikan indeks yang dimasukkan valid (tidak diluar batas list)
    if 0 <= indeks < len(data):
        angka_baru = int(input("Masukkan angka baru: "))
        # Mengganti nilai angka pada posisi indeks yang ditentukan
        data[indeks] = angka_baru
        print("Data berhasil diubah.")
    else:
        print("Indeks tidak valid.")
# Fungsi untuk menghapus angka berdasarkan nilai
def hapus():
    angka = int(input("Masukkan angka yang ingin dihapus: "))
    # Pengecekan: Apakah angka tersebut ada di dalam list
    if angka in data:
        # Menghapus kemunculan pertama dari angka tersebut
        data.remove(angka)
        print("Angka dihapus.")
    else:
        print("Angka tidak ditemukan.")
# Fungsi untuk memeriksa apakah list dapat dibagi menjadi duakelompok dengan jumlah yang sama
def cek_pembagian():
    total = sum(data)
    # Cek 1: Jika total ganjil, pembagian sama rata mustahil
    if total % 2 != 0:
        print(False)
        return
    target = total // 2
    subset = [] # Variabel ini tidak digunakan, bisa diabaikan
    # Fungsi rekursif: mencari subset yang jumlahnya sama dengan'target'
    def cari(jumlah, indeks):

        # Basis Kasus 1: Berhasil (Target ditemukan)
        if jumlah == target:
            return True
        # Basis Kasus 2: Gagal (Jumlah melebihi target atau sudah sampai akhir list)
        if jumlah > target or indeks == len(data):
            return False
        # Rekursi: Mencoba 1) Ambil angka saat ini ATAU 2) Jangan ambil angka saat ini
        return cari(jumlah + data[indeks], indeks + 1) or cari(jumlah, indeks + 1)
    # Memulai pencarian dan mencetak hasilnya (True/False)
    print(cari(0, 0))
# --- MAIN LOOP (Pengontrol Program) ---
while True:
    print()
    print("Menu:")
    print("1. Tambah angka")
    print("2. Tampilkan data")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek pembagian")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        ubah_angka()
    elif pilihan == "4":
        hapus()
    elif pilihan == "5":
        cek_pembagian()
    elif pilihan == "6":
        print("Program selesai.")
        # Menghentikan loop dan keluar dari program
        break
    else:
        print("Pilihan tidak valid.")