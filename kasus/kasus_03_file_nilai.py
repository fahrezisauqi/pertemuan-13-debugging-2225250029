
def baca_nilai(nama_file):
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            print(baris.strip())


baca_nilai("data_nilai.txt")
