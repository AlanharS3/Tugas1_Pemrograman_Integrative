import math

def pembagian_3():
    try:
        #Input bilangan bulat
        bilangan_bulat = int(input("Masukkan angka (bilangan bulat) : "))
        
        #Bagi 3 kemudian tampilkan ke desimal
        hasil = round(bilangan_bulat / 3, 3)
        
        #Print hasil
        print(f"Hasil pembagian {bilangan_bulat} dengan 3 adalah: {hasil}")

    except ValueError:
        print("Input tidak valid, Harap masukkan bilangan bulat")

if __name__ == "__main__":
    pembagian_3()
