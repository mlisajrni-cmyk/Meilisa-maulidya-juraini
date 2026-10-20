# 1. Input nilai tugas, UTS, UAS, dan kehadiran mahasiswa
tugas = float(input("Nilai tugas : "))
uts = float(input("Nilai UTS   : "))
uas = float(input("Nilai UAS   : "))
kehadiran = float(input("Kehadiran   : "))

# 2. Hitung nilai akhir dengan rumus di soal
nilai_akhir = (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)

# 3, 4, 5, 6. Logika Kelulusan dan Predikat
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

# Cetak Contoh Output
print(f"Nilai Akhir : {nilai_akhir}")
print(f"Status      : {status}")