def hitung_jumlah():

    try:
        #Masukkan input
        angka = int(input("Masukkan angka: "))
        
        #Sertakan detail penambahan
        rumus_jumlah = '+'.join(map(str, range(1, angka + 1)))
        
        #Menghitung nilai 
        total = sum(range(1, angka + 1))
        
        #Print hasil
        print(f"Penjumlahan dari nilai 1 hingga {angka} adalah: ({rumus_jumlah})")

        print(f"Hasil dari penjumlahannya adalah : {total}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    hitung_jumlah()
