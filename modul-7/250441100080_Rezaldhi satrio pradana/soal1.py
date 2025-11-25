buku_kontak = {}

def tambah_kontak():
    print("\nTAMBAH KONTAK BARU")
    nama = input("Masukkan Nama Kontak: ").strip().title()

    if nama in buku_kontak:
        print(f"Kontak dengan nama '{nama}' sudah ada.")
        return

    nomor_telepon = input("Masukkan Nomor Telepon: ").strip()
    alamat_email = input("Masukkan Alamat Email: ").strip()

    buku_kontak[nama] = [nomor_telepon, alamat_email]
    print(f"Kontak '{nama}' berhasil ditambahkan.")

def tampilkan_semua_kontak():
    print("\nDAFTAR SEMUA KONTAK")
    if not buku_kontak:
        print("Buku kontak kosong.")
        return

    print(f"{'Nama':<20}{'Nomor Telepon':<20}{'Email':<30}")
    for nama, data_kontak in buku_kontak.items():
        nomor_telepon_data, alamat_email_data = data_kontak
        print(f"{nama:<20}{nomor_telepon_data:<20}{alamat_email_data:<30}")

def cari_kontak():
    print("\n--- CARI KONTAK ---")
    nama = input("Masukkan Nama Kontak yang dicari: ").strip().title()

    if nama in buku_kontak:
        nomor_telepon, alamat_email = buku_kontak[nama]
        print(f"\n[ Detail Kontak: {nama} ]")
        print(f"Nomor Telepon: {nomor_telepon}")
        print(f"Email: {alamat_email}")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")

def perbarui_email_kontak():
    print("\n-PERBARUI EMAIL KONTAK")
    nama = input("Masukkan Nama Kontak yang ingin diubah emailnya: ").strip().title()

    if nama in buku_kontak:
        email_baru = input("Masukkan Alamat Email yang baru: ").strip()
        
        buku_kontak[nama][1] = email_baru
        print(f"Email kontak '{nama}' berhasil diperbarui.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan. Pembaruan dibatalkan.")

def hapus_kontak():
    """Menghapus kontak berdasarkan nama (Hapus/Delete)."""
    print("\nHAPUS KONTAK")
    nama = input("Masukkan Nama Kontak yang ingin dihapus: ").strip().title()

    if nama in buku_kontak:
        del buku_kontak[nama]
        print(f"Kontak '{nama}' berhasil dihapus.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan. Penghapusan dibatalkan.")
def menu_utama():
    """Menjalankan menu utama program Buku Kontak."""
    while True:
        print("   PROGRAM BUKU KONTAK (CRUD)")
        print("1. Tampilkan Semua Kontak")
        print("2. Cari Kontak")
        print("3. Tambah Kontak Baru")
        print("4. Perbarui Email Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ").strip()

        if pilihan == '1':
            tampilkan_semua_kontak()
        elif pilihan == '2':
            cari_kontak()
        elif pilihan == '3':
            tambah_kontak()
        elif pilihan == '4':
            perbarui_email_kontak()
        elif pilihan == '5':
            hapus_kontak()
        elif pilihan == '6':
            print("Program Buku Kontak selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()


