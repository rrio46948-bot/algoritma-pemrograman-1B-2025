def hitung_faktorial_rekursif(n):
    
    if n == 0 or n == 1:
        return 1
    
    elif n > 1:
        return n * hitung_faktorial_rekursif(n - 1)
    
    else:
        return "Input harus bilangan bulat non-negatif."
    

nilai_n = 5  
hasil = hitung_faktorial_rekursif(nilai_n)

print(f"Faktorial dari {nilai_n}! adalah: {hasil}")

print(f"Faktorial dari 7! adalah: {hitung_faktorial_rekursif(7)}")