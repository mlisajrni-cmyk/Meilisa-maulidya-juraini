# Data target nilai tiap mahasiswa
target_mahasiswa = {
    "andi": 70,
    "budi": 75,
    "citra": 80
}

# 1. Input nama dan tampilkan target
nama = input("Nama : ").strip()
kunci = nama .lower()

if kunci in target_mahasiswa:
    target = target_mahasiswa[kunci]
    print(f"Target nilai {nama}: {target}")

    # 2 & 3. Input nilai, ulangi maksimal 3 kali
    percobaan = 0
    lulus = False

    while percobaan < 3:
        percobaan += 1
        nilai = int(input(f"Nilai {percobaan} : "))

        if nilai >= target:
            lulus = True
            break

    # 4. Tampilkan hasil akhir
    if lulus:
        print(f"{nama} berhasil lulus setelah {percobaan} kali percobaan!")
    else:
        print(f"{nama} tidak lulus setelah 3 kali percobaan!")
else:
    print("Data mahasiswa tidak ditemukan.")
