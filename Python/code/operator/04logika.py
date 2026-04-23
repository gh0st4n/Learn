# OPERATOR LOGIKA

print("=== Operator Logika ===")

a = True
b = False

print("a =", a)
print("b =", b)
print()

# AND
print("a and b ->", a and b)  # False

# OR
print("a or b  ->", a or b)   # True

# NOT
print("not a   ->", not a)    # False
print("not b   ->", not b)    # True

print()


print("=== Contoh dengan Perbandingan ===")

x = 10

print("x > 5 and x < 20 ->", x > 5 and x < 20)  # True
print("x < 5 or x > 8  ->", x < 5 or x > 8)     # True
print("not (x > 5)     ->", not (x > 5))        # False

print()


print("=== Contoh Real Use ===")

umur = 18
punya_ktp = True

# Syarat boleh daftar
print("Boleh daftar? ->", umur >= 17 and punya_ktp)

# Syarat diskon
member = False
print("Dapat diskon? ->", umur < 12 or member)

print()


print("=== Behavior Penting (Short-Circuit) ===")

# AND: berhenti kalau sudah False
print(False and print("Ini tidak akan muncul"))

# OR: berhenti kalau sudah True
print(True or print("Ini juga tidak akan muncul"))

print()


print("=== Truthy & Falsy ===")

print("bool(0)     ->", bool(0))     # False
print("bool(1)     ->", bool(1))     # True
print("bool('')    ->", bool(''))    # False
print("bool('isi') ->", bool('isi')) # True
print("bool([])    ->", bool([]))    # False
print("bool([1])   ->", bool([1]))   # True

print()


print("=== Trick Python (Return Value) ===")

# Python tidak selalu return True/False
print("0 and 5  ->", 0 and 5)   # 0
print("5 and 10 ->", 5 and 10)  # 10

print("0 or 5   ->", 0 or 5)    # 5
print("5 or 10  ->", 5 or 10)   # 5