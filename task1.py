import math

def hitung_gaji_bulanan():
    try:
        #Input gaji tahunan
        gaji_tahunan = float(input("Masukkan gaji tahunan: "))
        
        #Menghitung gaji lalu dibulatkan
        gaji_bulanan = math.ceil(gaji_tahunan / 12)
        
        #Print hasil
        print(f"Gaji bulanan : {gaji_bulanan}")

    except ValueError:
        print("Input tidak valid, Harap masukkan bilangan yang valid.")

if __name__ == "__main__":
    hitung_gaji_bulanan()
