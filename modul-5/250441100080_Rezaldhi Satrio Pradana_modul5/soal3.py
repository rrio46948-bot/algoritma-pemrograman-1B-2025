def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    
    jabatan_lower = jabatan.lower() 
    
    if jabatan_lower == "manager":
        persentase_tunjangan = 0.10  
    elif jabatan_lower == "staff":
        persentase_tunjangan = 0.05
    else:
        persentase_tunjangan = 0.00
    
    jumlah_tunjangan = gaji_pokok * persentase_tunjangan
    jumlah_pph = gaji_pokok * 0.05
    
    gaji_kotor = gaji_pokok + jumlah_tunjangan
    gaji_bersih = gaji_kotor - jumlah_pph
    
    print("         SLIP GAJI BULANAN")
    print(f"Nama Karyawan    : {nama.upper()}")
    print(f"Jabatan          : {jabatan.title()}")
    print(f"Gaji Pokok       : Rp {gaji_pokok:,.0f}")
    print(f"Tunjangan ({persentase_tunjangan*100:.0f}%) : Rp {jumlah_tunjangan:,.0f}")
    print(f"PPh (5%)         : - Rp {jumlah_pph:,.0f}")
    print(f"**Gaji Bersih** : **Rp {gaji_bersih:,.0f}**")


print("--- Masukkan Data Karyawan ---")
nama_karyawan = input("Masukkan Nama Karyawan: ")
jabatan_karyawan = input("Masukkan Jabatan (Manager/Staff/Lainnya): ")

gaji_pokok_karyawan = float(input("Masukkan Gaji Pokok Bulanan (Angka): "))

hitung_gaji_bersih(nama_karyawan, jabatan_karyawan, gaji_pokok_karyawan)