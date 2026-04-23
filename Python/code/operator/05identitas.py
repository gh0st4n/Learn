# OPERATOR IDENTITAS

print("=== Operator Identitas ===")

a = [1, 2]
b = [1, 2]
c = a

print("a:", a)
print("b:", b)
print("c:", c)
print()

# Bandingkan VALUE
print("a == b ->", a == b)  # True (isi sama)

# Bandingkan OBJECT (memory)
print("a is b ->", a is b)  # False (objek berbeda)
print("a is c ->", a is c)  # True (referensi sama)

print()


print("=== is not ===")

print("a is not b ->", a is not b)  # True
print("a is not c ->", a is not c)  # False

print()


print("=== Contoh dengan None ===")

x = None

print("x is None ->", x is None)       # True
print("x == None ->", x == None)      # True (tapi tidak direkomendasikan)

# Best practice:
if x is None:
    print("x kosong (None)")

print()


print("=== Contoh Mutable Object ===")

a = [1, 2]
b = a

a.append(3)

print("a:", a)  # [1, 2, 3]
print("b:", b)  # ikut berubah (karena referensi sama)
print("a is b ->", a is b)  # True

print()


print("=== Contoh Immutable Object ===")

x = 10
y = 10

print("x == y ->", x == y)  # True
print("x is y ->", x is y)  # Bisa True (Python cache integer kecil)

print()


print("=== Hati-hati dengan is ===")

x = 1000
y = 1000

print("x == y ->", x == y)  # True
print("x is y ->", x is y)  # Bisa False (objek beda)
