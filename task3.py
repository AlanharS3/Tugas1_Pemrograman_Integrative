def tentukan_ukuran():

    try:
        #Masukkan Input
        angka = float(input("Masukkan angka: "))
        
        #Tentukan kategori
        if angka < 100:
            ukuran = "Kecil"
        elif 100 <= angka <= 200:
            ukuran = "Sedang"
        else:
            ukuran = "Besar"
        
        #Print hasil
        print(f"Kategori ukuran untuk {angka} adalah: {ukuran}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    tentukan_ukuran()
