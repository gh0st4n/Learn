# Variabel

name = "Miftahul Jannah"    # Tipe Data String
age = 17                    # Tipe Data Inteege
ting = 160.1                # Tipe Data Float

# Cara Menggabungkan Variabel dengan Text ada dua cara
# 1. Menggunakan Koma `print("Text", Variabel)`
# 2. Menggunakan f-string `print(f"Text {Variabel}")`
print(f"Nama : {name}")
print("Umur :",age, "Tahun")
print(f"Tinggi : {ting}")
print()

# Membuat Multi Variabel Dengan Multi Value Pada Satu Line
a, b, c, d = "ikki", 16, 160.1, False
print(f"Nama Teman {name} = {a}")
print(f"Umur {a} = {b}")
print(f"Tinngi {a} = {c}")
print(f"Status Pelajar = {d}")
print()

# Membuat Multi Variabel Dengan Satu Value
d = e = f = 1
print("d adalah nomor ", d)  # 1
print("e adalah nomor ", e)  # 1
print("f adalah nomor ", f)  # 1