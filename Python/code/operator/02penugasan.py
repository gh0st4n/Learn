# OPERATOR PENUGASAN PYTHON

print("=== Penugasan Dasar ===")
x = 10
print("x =", x)
print()


print("=== Penugasan dengan Operasi ===")

x = 5
x += 3
print("x += 3 ->", x)  # 8

x = 5
x -= 2
print("x -= 2 ->", x)  # 3

x = 4
x *= 3
print("x *= 3 ->", x)  # 12

x = 10
x /= 2
print("x /= 2 ->", x)  # 5.0

x = 7
x //= 2
print("x //= 2 ->", x)  # 3

x = 7
x %= 3
print("x %= 3 ->", x)  # 1

x = 2
x **= 3
print("x **= 3 ->", x)  # 8

print("=== Contoh Real Use ===")

# Counter
count = 0
count += 1
count += 1
print("Counter:", count)  # 2

# Akumulasi
total = 0
total += 100
total += 250
total -= 50
print("Total:", total)  # 300

# # Loop
# x = 1
# for _ in range(5):
#     x *= 2
# print("Loop x:", x)  # 32

print()


print("=== Behavior pada Mutable Object ===")

a = [1, 2]
b = a

a += [3]

print("a:", a)  # [1, 2, 3]
print("b:", b)  # ikut berubah (referensi sama)