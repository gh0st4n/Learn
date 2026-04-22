# Data Type
## String
nama = "Gh0sT4n"
nama_pr:str = "Miftah"
print("=== String Data Type ===")
print(f"Nama : {nama}, Data Type : {type(nama)}")
print(f"Nama : {nama_pr}, Data Type : {type(nama_pr)}")

## Numeric
integer = 17
integer2:int = 18
Fl = 3.14
fl:float = 160.3
Com = 1j
com:complex = 5j
cOm = complex(3j)

print("\n=== Numeric Data Type ===")
print(f"Integer : {integer}, Data Type : {type(integer)}")
print(f"Integer : {integer2}, Data Type : {type(integer2)}")
print(f"Float : {Fl}, Data Type : {type(Fl)}")
print(f"Float : {fl}, Data Type : {type(fl)}")
print(f"Complex : {Com}, Data Type : {type(Com)}")
print(f"Complex : {cOm}, Data Type : {type(cOm)}")
print(f"Complex : {com}, Data Type : {type(com)}")

## Boolean
Bool1 = True
Bool2 = False
Bool3:bool = True
Bool4:bool = False

print("\n=== Boolean Data Type ===")
print(f"Boolean : {Bool1}, Data Type : {type(Bool1)}")
print(f"Boolean : {Bool2}, Data Type : {type(Bool2)}")
print(f"Boolean : {Bool3}, Data Type : {type(Bool3)}")
print(f"Boolean : {Bool4}, Data Type : {type(Bool4)}")

## List
"""
Perhitungan List Menggunakan index array[0, 1, 2, ..]
"""
nama = ['T4n OS', 'Gh0sT4n']
umur = [20, 30]

print("\n=== List Data Type ===")
print(nama)
print(umur)
print(f"Nama : {nama[1]}, Data Type : {type(nama)}")
print(f"Umur : {umur[0]}, Data Type : {type(umur)}")

## Tuple
"""
Perhitungan Tuple Menggunakan index array[0, 1, 2, ..]
"""
Tp = ('T4n OS', 'Gh0sT4n')
tp = (20, 30)

print("\n=== List Data Type ===")
print(Tp)
print(tp)
print(f"Tuple1 : {Tp[1]}, Data Type : {type(Tp)}")
print(f"Tuple2 : {tp[0]}, Data Type : {type(tp)}")

## Set
SS = {'Gh0sT4n', 'arfy slowly'}
Ss:set = {18, 19}

print("\n=== Set Data Type ===")
print(SS)
print(Ss)
print(f"SS1 : {SS}, Data Type : {type(SS)}")
print(f"Ss2 : {Ss}, Data Type : {type(Ss)}")

## Frozenset
FS = {'Gh0sT4n', 'arfy slowly'}
fs:frozenset = {18, 19}

print("\n=== FrozenSet Data Type ===")
print(FS)
print(fs)
print(f"FS : {FS}, Data Type : {type(FS)}")
print(f"fs : {fs}, Data Type : {type(fs)}")

## Dictionary
test1 = {"nama": "Andi", "usia": 25}
hari = {
    "sen": "senin",
    "sel": "selasa",
    "rab": "rabu"
}

bulan:dict = {
    "jan": "january",
    "feb": "februari",
    "mar": "maret"
}

print("\n=== FrozenSet Data Type ===")
print(test1)
print(hari)
print(bulan)
print()
print(f"test1 : {test1}, Data Type : {type(test1)}")
print(f"hari  : {hari},  Data Type : {type(hari)}")
print(f"bulan : {bulan}, Data Type : {type(bulan)}")
print()
print(f"test1 : {test1["nama"]}, Data Type : {type(test1["nama"])}")
print(f"hari  : {hari["sel"]},   Data Type : {type(hari["sel"])}")
print(f"bulan : {bulan["mar"]},  Data Type : {type(bulan["mar"])}")

## Binary
By = bytes(17)
#By1:bytes = 17 # int
Bya = bytearray(18)
ByA:bytearray = 18 #> int
# Mv = memoryview(18) # TypeError: memoryview: a bytes-like object is required, not 'int'
Mv1:memoryview = 18
Mvw = memoryview(bytes(18))
Mvw1:memoryview = bytes(18)

print("\n=== Binary Data Type ===")
print(f"Bytes : {By}, Data Type : {type(By)}")
#print(f"Bytes : {By1}, Data Type : {type(By1)}") # int
print(f"Bytesarray {Bya}, Data Type : {type(Bya)}")
#print(f"Bytesarray {ByA}, Data Type : {type(ByA)}") # int
#print(Mv)
print(f"Memoryview : {Mv1}, Data Type : {type(Mvw1)}") # Bytes
print(f"Memoryview : {Mvw}, Data Type : {type(Mvw)}") # Memoryview
print(f"Memoryview : {Mvw1}, Data Type : {type(Mvw1)}") # Bytes