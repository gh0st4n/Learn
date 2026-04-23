# OPERATOR PERBANDINGAN

print("=== Operator Perbandingan ===")

a = 5
b = 3

print("a =", a)
print("b =", b)
print()

# Sama dengan
print("a == b ->", a == b)  # False

# Tidak sama
print("a != b ->", a != b)  # True

# Lebih besar
print("a > b  ->", a > b)   # True

# Lebih kecil
print("a < b  ->", a < b)   # False

# Lebih besar atau sama
print("a >= b ->", a >= b)  # True

# Lebih kecil atau sama
print("a <= b ->", a <= b)  # False

print()


print("=== Contoh Real Use ===")

nilai = 75

# Cek lulus
print("Lulus? ->", nilai >= 70)

# Cek nilai perfect
print("Nilai sempurna? ->", nilai == 100)

# Range check
print("Nilai di antara 60-80? ->", 60 <= nilai <= 80)

print()


print("=== Perbandingan String ===")

x = "apple"
y = "banana"

print("x == y ->", x == y)  # False
print("x < y  ->", x < y)   # True (berdasarkan alfabet)

print()


print("=== Perbandingan List ===")

a = [1, 2]
b = [1, 2]
c = [1, 2, 3]

print("a == b ->", a == b)  # True (isi sama)
print("a == c ->", a == c)  # False

print()


print("=== Catatan Penting ===")

# == membandingkan VALUE
# is membandingkan OBJECT (alamat memory)

a = [1, 2]
b = [1, 2]

print("a == b ->", a == b)  # True
print("a is b ->", a is b)  # False (objek berbeda)