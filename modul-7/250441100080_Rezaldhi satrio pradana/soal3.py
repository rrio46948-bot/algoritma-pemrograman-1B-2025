data_kupon = {
    "HEMAT10": 10,
    "SUPER20": 20,
    "DISKON50": 50,
    "JUMATBERKAH": 75
}

while True:
    print("    SISTEM KASIR & KERANJANG      ")
    print("1. Cek Daftar Kupon")
    print("2. Mulai Transaksi (Belanja)")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        print("\nKupon Tersedia")
        if len(data_kupon) > 0:
            for kode, diskon in data_kupon.items():
                print(f"- {kode} : Diskon {diskon}%")
        else:
            print("Semua kupon sudah habis.")

    elif pilihan == "2":
        print("\n--- Masukkan Barang Belanjaan ---")
        
        total_belanja = 0
        daftar_barang = []  
        while True:
            nama_barang = input("Nama Barang : ").strip().title()
            
            try:
                harga_barang = float(input(f"Harga {nama_barang}: Rp "))
            except ValueError:
                print("Harga harus angka! Ulangi input barang ini.")
                continue
            
            daftar_barang.append(f"{nama_barang:<15} : Rp {harga_barang:,.0f}")
            total_belanja += harga_barang
            
            print(f"--> '{nama_barang}' masuk keranjang. Subtotal: Rp {total_belanja:,.0f}")

            lanjut = input("Tambah barang lain? (y/tidak): ").lower()
            if lanjut != 'y':
                break 

        print(f"\nTotal Belanja Sementara: Rp {total_belanja:,.0f}")
        kode_input = input("Punya kode kupon? (Tekan Enter jika tidak ada): ").upper().strip()

        potongan = 0
        persen = 0
        status_kupon = "Tidak Ada"

        if kode_input in data_kupon:
            persen = data_kupon[kode_input]
            potongan = (persen / 100) * total_belanja
            status_kupon = kode_input
            
            del data_kupon[kode_input]
            print(f"Kupon '{kode_input}' BERHASIL dipasang!")
            
        elif kode_input != "":
            print(f"Kupon '{kode_input}' TIDAK VALID atau sudah terpakai.")

        total_bayar = total_belanja - potongan

        print("\n" + "="*30)
        print("      STRUK PEMBAYARAN      ")
        print("="*30)
        
        for item in daftar_barang:
            print(item)
        print("-" * 30)
        print(f"Total Awal   : Rp {total_belanja:,.0f}")
        print(f"Diskon ({persen}%) : Rp {potongan:,.0f}")
        print(f"Total Akhir  : Rp {total_bayar:,.0f}")
        print("="*30)
        print("Terima kasih sudah berbelanja!\n")

    elif pilihan == "3":
        print("Program selesai.")
        break
    
    else:
        print("Pilihan tidak valid.")