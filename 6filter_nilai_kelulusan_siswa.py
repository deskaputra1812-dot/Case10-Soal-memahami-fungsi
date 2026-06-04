def apakah_lulus(nilai_siswa, nilai_kkm):
    if nilai_siswa >= nilai_kkm :
        return True
    else :
        return False

nilai_siswa = int(input("Masukkan Jumlah Nilai Siswa: "))
nilai_kkm = 75

hasil = apakah_lulus(nilai_siswa, nilai_kkm)

print(hasil)