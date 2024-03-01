def hitung_sum():
    total_sum = 0

    print("Masukkan angka. Masukkan -1 jika selesai :")

    while True:
        try:
            #Masukkan input
            angka = float(input())
            
            #Memerikasa jika ada angka -1, looping akan berhenti
            if angka == -1:
                break

            # Menambahkan jumlah angka 
            total_sum += angka

        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    #Print hasil
    print(f"Jumlahnya : {total_sum}")

if __name__ == "__main__":
    hitung_sum()
