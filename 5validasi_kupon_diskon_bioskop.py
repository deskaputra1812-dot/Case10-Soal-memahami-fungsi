def cek_diskon(total_harga, jumlah_tiket, kode_kupon) :
    if kode_kupon == "NONTONSERU" and jumlah_tiket >= 2 :
         diskon = total_harga - 15000
    else :
         diskon = total_harga
    return diskon

total_harga = int(input("masukan total harga: "))
jumlah_tiket = int(input("masukan jumlah tiket: "))
kode_kupon = input("masukan kupon: ")

hasil = cek_diskon(total_harga, jumlah_tiket, kode_kupon)

print("harga akhir yang harus dibayar pembeli adalah", hasil)
