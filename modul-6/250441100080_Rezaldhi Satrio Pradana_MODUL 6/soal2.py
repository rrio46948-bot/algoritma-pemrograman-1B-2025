tuple_angka_a = (3, 1, 4)
tuple_angka_b = (1, 5, 9)
def proses_tuple(tup_a, tup_b):
    gabungan = tup_a + tup_b
    print(f"Langkah 1: Gabungan Awal: {gabungan}")
    tanpa_duplikat = []
    for angka in gabungan:
        if angka not in tanpa_duplikat:
            tanpa_duplikat.append(angka)
    print(f"Langkah 2: Hapus Duplikat (List): {tanpa_duplikat}")

    n = len(tanpa_duplikat)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tanpa_duplikat[j] < tanpa_duplikat[j + 1]:
                tanpa_duplikat[j], tanpa_duplikat[j + 1] =tanpa_duplikat[j + 1], tanpa_duplikat[j]
    hasil_akhir = tuple(tanpa_duplikat)
    return hasil_akhir
print("--- Mulai Pemrosesan Tuple ---")
hasil_tuple_akhir = proses_tuple(tuple_angka_a, tuple_angka_b)
print("\n---")
print(f"Hasil Akhir yang Diminta: **{hasil_tuple_akhir}**")
print("---")