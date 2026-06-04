def format_alamat(jalan, kota, provinsi, kode_pos):
    alamat =f"Jalan {jalan}, Kota {kota}, {provinsi}, ({kode_pos})"
    return alamat

jalan = input("Masukkan nama jalan: ")
kota = input("Masukkan nama kota: ")
provinsi = input("Masukkan nama provinsi: ")
kode_pos = int(input("Masukkan kode pos: "))

hasil =  format_alamat(jalan, kota, provinsi, kode_pos)

print(hasil)