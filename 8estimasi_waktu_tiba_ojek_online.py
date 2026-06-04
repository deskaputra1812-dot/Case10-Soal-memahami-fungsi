def estimasi_tiba(jarak_km, kondisi_cuaca):
    waktu_per1kilo = jarak_km * 3
    if kondisi_cuaca == "hujan":
        waktu_per1kilo += 10
     
    return waktu_per1kilo

jarak_km = int(input("Masukkan jumlah Jarak KM: "))
kondisi_cuaca = input("Masukkan Kondisi Cuaca: ")

hasil = estimasi_tiba(jarak_km, kondisi_cuaca)

print(f"{hasil} menit")