def cek_anagram(kata1, kata2):
    
    
    bersih_kata1 = kata1.replace(" ", "").lower()
    bersih_kata2 = kata2.replace(" ", "").lower()
    
    if len(bersih_kata1) != len(bersih_kata2):
        return False
        
    
    kata1_sorted = sorted(bersih_kata1)
    kata2_sorted = sorted(bersih_kata2)
    
    if kata1_sorted == kata2_sorted:
        return True
    else:
        return False

kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

hasil_boolean = cek_anagram(kata_pertama, kata_kedua)

print("\n--- Hasil Pengecekan ---")

if hasil_boolean:
    print(f"Kata '{kata_pertama}' dan '{kata_kedua}' adalah **ANAGRAM**.")
else:
    print(f"Kata '{kata_pertama}' dan '{kata_kedua}' **bukan** anagram.")