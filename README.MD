# Python Learning Guide / Panduan Belajar Python

## Table of Contents / Daftar Isi
- [English Version](#english-version)
  - [1. Conditions](#1-conditions)
  - [2. Loops](#2-loops)
  - [3. Functions](#3-functions)
  - [4. Data Structures](#4-data-structures)
  - [5. Classes](#5-classes)
- [Indonesian Version / Versi Bahasa Indonesia](#indonesian-version--versi-bahasa-indonesia)
  - [1. Kondisi](#1-kondisi)
  - [2. Perulangan](#2-perulangan)
  - [3. Fungsi](#3-fungsi)
  - [4. Struktur Data](#4-struktur-data)
  - [5. Kelas](#5-kelas)

---

## English Version

### 1. Conditions

Conditions allow your program to make decisions based on different scenarios.

#### Basic If Statement
```python
age = 18
if age >= 18:
    print("You are an adult")
```

#### If-Else Statement
```python
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")
```

#### If-Elif-Else Statement
```python
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

#### Comparison Operators
- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

#### Logical Operators
```python
# AND operator
age = 25
income = 50000
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# OR operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# NOT operator
is_raining = False
if not is_raining:
    print("Go for a walk")
```

---

### 2. Loops

Loops allow you to repeat code multiple times.

#### For Loop
```python
# Loop through numbers
for i in range(5):
    print(f"Number: {i}")

# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop with start, stop, step
for i in range(2, 10, 2):  # Start=2, Stop=10, Step=2
    print(i)  # Prints: 2, 4, 6, 8
```

#### While Loop
```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

#### Loop Control Statements
```python
# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints: 0, 1, 2, 3, 4

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints: 0, 1, 3, 4
```

#### Nested Loops
```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

---

### 3. Functions

Functions are reusable blocks of code that perform specific tasks.

#### Basic Function
```python
def greet():
    print("Hello, World!")

greet()  # Call the function
```

#### Function with Parameters
```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
```

#### Function with Return Value
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8
```

#### Function with Default Parameters
```python
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))  # Hello, Mr. Smith!
print(greet_with_title("Johnson", "Dr."))  # Hello, Dr. Johnson!
```

#### Function with Multiple Return Values
```python
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

sum_result, diff_result = calculate(10, 3)
print(f"Sum: {sum_result}, Difference: {diff_result}")
```

#### Lambda Functions (Anonymous Functions)
```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

---

### 4. Data Structures

Python provides several built-in data structures to organize and store data.

#### Lists
```python
# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, True, 3.14]

# List operations
fruits.append("grape")  # Add to end
fruits.insert(1, "mango")  # Insert at index
fruits.remove("banana")  # Remove by value
popped_item = fruits.pop()  # Remove and return last item

# List methods
print(len(fruits))  # Length
print(fruits[0])  # First item
print(fruits[-1])  # Last item
print(fruits[1:3])  # Slicing

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

#### Tuples
```python
# Creating tuples (immutable)
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# Tuple operations
x, y = coordinates  # Unpacking
print(f"X: {x}, Y: {y}")

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: {p.x}, {p.y}")
```

#### Dictionaries
```python
# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Dictionary operations
student["email"] = "alice@email.com"  # Add key-value
student["age"] = 21  # Update value
del student["grade"]  # Delete key

# Dictionary methods
print(student.keys())    # Get all keys
print(student.values())  # Get all values
print(student.items())   # Get key-value pairs

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### Sets
```python
# Creating sets (unique elements)
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}

# Set operations
colors.add("yellow")
colors.remove("red")
colors.discard("purple")  # Won't raise error if not found

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2))   # {1, 2}
```

---

### 5. Classes

Classes are blueprints for creating objects with attributes and methods.

#### Basic Class
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is a {self.breed}"

# Creating objects
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())      # Buddy says Woof!
print(my_dog.get_info())  # Buddy is a Golden Retriever
```

#### Class with Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(f"Area: {circle.area}")  # Area: 78.53975
circle.radius = 10
print(f"New area: {circle.area}")  # New area: 314.159
```

#### Inheritance
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass
    
    def get_info(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed
    
    def make_sound(self):
        return "Meow!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"

# Using inheritance
cat = Cat("Whiskers", "Persian")
dog = Dog("Rex", "German Shepherd")

print(cat.get_info())    # Whiskers is a Cat
print(cat.make_sound())  # Meow!
print(dog.make_sound())  # Woof!
```

#### Class Methods and Static Methods
```python
class MathUtils:
    pi = 3.14159
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @classmethod
    def get_pi(cls):
        return cls.pi
    
    @staticmethod
    def circle_area(radius):
        return MathUtils.pi * radius ** 2

# Using static and class methods
print(MathUtils.add(5, 3))        # 8
print(MathUtils.get_pi())         # 3.14159
print(MathUtils.circle_area(5))   # 78.53975
```

---

## Indonesian Version / Versi Bahasa Indonesia

### 1. Kondisi

Kondisi memungkinkan program Anda membuat keputusan berdasarkan skenario yang berbeda.

#### Pernyataan If Dasar
```python
umur = 18
if umur >= 18:
    print("Anda sudah dewasa")
```

#### Pernyataan If-Else
```python
suhu = 25
if suhu > 30:
    print("Cuaca panas di luar")
else:
    print("Cuaca tidak terlalu panas")
```

#### Pernyataan If-Elif-Else
```python
nilai = 85
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")
```

#### Operator Perbandingan
- `==` : Sama dengan
- `!=` : Tidak sama dengan
- `>` : Lebih besar dari
- `<` : Lebih kecil dari
- `>=` : Lebih besar atau sama dengan
- `<=` : Lebih kecil atau sama dengan

#### Operator Logika
```python
# Operator AND
umur = 25
penghasilan = 50000
if umur >= 18 and penghasilan >= 30000:
    print("Memenuhi syarat untuk pinjaman")

# Operator OR
hari = "Sabtu"
if hari == "Sabtu" or hari == "Minggu":
    print("Ini akhir pekan!")

# Operator NOT
sedang_hujan = False
if not sedang_hujan:
    print("Pergi jalan-jalan")
```

---

### 2. Perulangan

Perulangan memungkinkan Anda mengulangi kode beberapa kali.

#### Perulangan For
```python
# Perulangan melalui angka
for i in range(5):
    print(f"Angka: {i}")

# Perulangan melalui list
buah_buahan = ["apel", "pisang", "jeruk"]
for buah in buah_buahan:
    print(f"Saya suka {buah}")

# Perulangan dengan start, stop, step
for i in range(2, 10, 2):  # Start=2, Stop=10, Step=2
    print(i)  # Mencetak: 2, 4, 6, 8
```

#### Perulangan While
```python
# Perulangan while dasar
hitung = 0
while hitung < 5:
    print(f"Hitungan: {hitung}")
    hitung += 1

# Perulangan while dengan input pengguna
kata_sandi = ""
while kata_sandi != "rahasia":
    kata_sandi = input("Masukkan kata sandi: ")
print("Akses diberikan!")
```

#### Pernyataan Kontrol Perulangan
```python
# Pernyataan break
for i in range(10):
    if i == 5:
        break
    print(i)  # Mencetak: 0, 1, 2, 3, 4

# Pernyataan continue
for i in range(5):
    if i == 2:
        continue
    print(i)  # Mencetak: 0, 1, 3, 4
```

#### Perulangan Bersarang
```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

---

### 3. Fungsi

Fungsi adalah blok kode yang dapat digunakan kembali untuk melakukan tugas tertentu.

#### Fungsi Dasar
```python
def sapa():
    print("Halo, Dunia!")

sapa()  # Memanggil fungsi
```

#### Fungsi dengan Parameter
```python
def sapa_orang(nama):
    print(f"Halo, {nama}!")

sapa_orang("Alice")
```

#### Fungsi dengan Nilai Kembali
```python
def tambah_angka(a, b):
    return a + b

hasil = tambah_angka(5, 3)
print(hasil)  # Output: 8
```

#### Fungsi dengan Parameter Default
```python
def sapa_dengan_gelar(nama, gelar="Pak"):
    return f"Halo, {gelar} {nama}!"

print(sapa_dengan_gelar("Smith"))  # Halo, Pak Smith!
print(sapa_dengan_gelar("Johnson", "Dr."))  # Halo, Dr. Johnson!
```

#### Fungsi dengan Banyak Nilai Kembali
```python
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

hasil_jumlah, hasil_kurang = hitung(10, 3)
print(f"Jumlah: {hasil_jumlah}, Selisih: {hasil_kurang}")
```

#### Fungsi Lambda (Fungsi Anonim)
```python
# Lambda dasar
kuadrat = lambda x: x ** 2
print(kuadrat(5))  # Output: 25

# Lambda dengan banyak parameter
kali = lambda x, y: x * y
print(kali(3, 4))  # Output: 12

# Menggunakan lambda dengan fungsi built-in
angka = [1, 2, 3, 4, 5]
angka_kuadrat = list(map(lambda x: x**2, angka))
print(angka_kuadrat)  # Output: [1, 4, 9, 16, 25]
```

---

### 4. Struktur Data

Python menyediakan beberapa struktur data built-in untuk mengorganisir dan menyimpan data.

#### List
```python
# Membuat list
buah_buahan = ["apel", "pisang", "jeruk"]
angka = [1, 2, 3, 4, 5]
list_campuran = ["halo", 42, True, 3.14]

# Operasi list
buah_buahan.append("anggur")  # Tambah di akhir
buah_buahan.insert(1, "mangga")  # Sisipkan di indeks
buah_buahan.remove("pisang")  # Hapus berdasarkan nilai
item_keluar = buah_buahan.pop()  # Hapus dan kembalikan item terakhir

# Method list
print(len(buah_buahan))  # Panjang
print(buah_buahan[0])  # Item pertama
print(buah_buahan[-1])  # Item terakhir
print(buah_buahan[1:3])  # Slicing

# List comprehension
kuadrat = [x**2 for x in range(5)]
print(kuadrat)  # Output: [0, 1, 4, 9, 16]
```

#### Tuple
```python
# Membuat tuple (tidak dapat diubah)
koordinat = (10, 20)
warna_rgb = (255, 128, 0)

# Operasi tuple
x, y = koordinat  # Unpacking
print(f"X: {x}, Y: {y}")

# Named tuple
from collections import namedtuple
Titik = namedtuple('Titik', ['x', 'y'])
p = Titik(10, 20)
print(f"Titik: {p.x}, {p.y}")
```

#### Dictionary
```python
# Membuat dictionary
siswa = {
    "nama": "Alice",
    "umur": 20,
    "nilai": "A"
}

# Operasi dictionary
siswa["email"] = "alice@email.com"  # Tambah key-value
siswa["umur"] = 21  # Update nilai
del siswa["nilai"]  # Hapus key

# Method dictionary
print(siswa.keys())    # Dapatkan semua key
print(siswa.values())  # Dapatkan semua value
print(siswa.items())   # Dapatkan pasangan key-value

# Dictionary comprehension
kuadrat_dict = {x: x**2 for x in range(5)}
print(kuadrat_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### Set
```python
# Membuat set (elemen unik)
angka_unik = {1, 2, 3, 4, 5}
warna = {"merah", "hijau", "biru"}

# Operasi set
warna.add("kuning")
warna.remove("merah")
warna.discard("ungu")  # Tidak akan error jika tidak ditemukan

# Operasi set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2))   # {1, 2}
```

---

### 5. Kelas

Kelas adalah blueprint untuk membuat objek dengan atribut dan method.

#### Kelas Dasar
```python
class Anjing:
    def __init__(self, nama, ras):
        self.nama = nama
        self.ras = ras
    
    def gonggong(self):
        return f"{self.nama} menggonggong Guk!"
    
    def dapat_info(self):
        return f"{self.nama} adalah {self.ras}"

# Membuat objek
anjing_saya = Anjing("Buddy", "Golden Retriever")
print(anjing_saya.gonggong())      # Buddy menggonggong Guk!
print(anjing_saya.dapat_info())  # Buddy adalah Golden Retriever
```

#### Kelas dengan Properties
```python
class Lingkaran:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, nilai):
        if nilai < 0:
            raise ValueError("Radius tidak boleh negatif")
        self._radius = nilai
    
    @property
    def luas(self):
        return 3.14159 * self._radius ** 2

lingkaran = Lingkaran(5)
print(f"Luas: {lingkaran.luas}")  # Luas: 78.53975
lingkaran.radius = 10
print(f"Luas baru: {lingkaran.luas}")  # Luas baru: 314.159
```

#### Pewarisan (Inheritance)
```python
class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies
    
    def buat_suara(self):
        pass
    
    def dapat_info(self):
        return f"{self.nama} adalah {self.spesies}"

class Kucing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama, "Kucing")
        self.ras = ras
    
    def buat_suara(self):
        return "Meong!"

class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama, "Anjing")
        self.ras = ras
    
    def buat_suara(self):
        return "Guk!"

# Menggunakan inheritance
kucing = Kucing("Whiskers", "Persia")
anjing = Anjing("Rex", "German Shepherd")

print(kucing.dapat_info())    # Whiskers adalah Kucing
print(kucing.buat_suara())  # Meong!
print(anjing.buat_suara())  # Guk!
```

#### Method Kelas dan Method Statis
```python
class UtilMatematika:
    pi = 3.14159
    
    @staticmethod
    def tambah(x, y):
        return x + y
    
    @classmethod
    def dapat_pi(cls):
        return cls.pi
    
    @staticmethod
    def luas_lingkaran(radius):
        return UtilMatematika.pi * radius ** 2

# Menggunakan method statis dan kelas
print(UtilMatematika.tambah(5, 3))        # 8
print(UtilMatematika.dapat_pi())         # 3.14159
print(UtilMatematika.luas_lingkaran(5))   # 78.53975
```

---

## Additional Resources 

### English Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)

### Sumber Bahasa Indonesia
- [Tutorial Python Bahasa Indonesia](https://tutorial.python.web.id/)
- [Belajar Python](https://www.pythonindo.com/)
- [Python ID](https://www.python.org/community/localsigs/#indonesia)

---

## Contributing 

Feel free to contribute to this learning guide by submitting pull requests or opening issues.
