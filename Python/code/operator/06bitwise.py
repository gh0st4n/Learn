# =========================
# OPERATOR BITWISE
# =========================

print("=== Operator Bitwise ===")

a = 5   # 0101 (binary)
b = 3   # 0011 (binary)

print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))
print()

# AND (&)
print("a & b  ->", a & b,  "->", bin(a & b))   # 0001 = 1

# OR (|)
print("a | b  ->", a | b,  "->", bin(a | b))   # 0111 = 7

# XOR (^)
print("a ^ b  ->", a ^ b,  "->", bin(a ^ b))   # 0110 = 6

# NOT (~)
print("~a     ->", ~a,     "->", bin(~a))      # -6 (two's complement)

print()


print("=== Shift Operator ===")

x = 5  # 0101

# Shift kiri (<<)
print("x << 1 ->", x << 1, "->", bin(x << 1))  # 1010 = 10

# Shift kanan (>>)
print("x >> 1 ->", x >> 1, "->", bin(x >> 1))  # 0010 = 2

print()


print("=== Contoh Real Use ===")

# Cek apakah angka genap (bit terakhir = 0)
n = 4
print("Genap? ->", (n & 1) == 0)

# Set bit (nyalakan bit tertentu)
flags = 0
flags |= 1   # set bit ke-1
flags |= 2   # set bit ke-2
print("flags ->", flags, bin(flags))

# Cek bit
print("bit 1 aktif? ->", (flags & 1) != 0)
print("bit 2 aktif? ->", (flags & 2) != 0)

# Toggle bit
flags ^= 1
print("toggle bit 1 ->", flags, bin(flags))

# Hapus bit
flags &= ~2
print("hapus bit 2 ->", flags, bin(flags))

print()


print("=== Catatan Penting ===")

# Bitwise hanya untuk integer
# Python pakai two's complement untuk bilangan negatif

print("bin(-1) ->", bin(-1))
print("~0      ->", ~0)  # -1