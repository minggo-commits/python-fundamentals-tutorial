# """Create program for:
# 1. print number 1 to 20,
# 2. Skip number which divisible by 3,
# 3. Stop loop if number was more than 15. """

# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     if i >= 15:
#         break
#     print(i)

# print("-----------------------------------------------------------------------")

# """Buat program yang menampilkan pola segitiga bintang seperti ini:
# *
# **
# ***
# ****
# *****
# """

# for j in range(1, 6):
#     print(j*"*")
    
# print("-----------------------------------------------------------------------")
# """Buat pola bintang terbalik:
# *****
# ****
# ***
# **
# *
# """

# for k in range(5, 0, -1):
#     print(k*("*"))

# print("-----------------------------------------------------------------------")

# #or
# k = 5
# x = "*"
# while k > 0:
#     print(k*x)
#     k += -1

from exercise.soal_1 import soal_1

def test_soal_1():
    expected = [1,2,3,4,5,6,7,8,9,10]
    result = soal_1()
    assert result == expected, f"Expected {expected} but got {result}"
    print('✅ Test soal_1 Pass')
  

if __name__ == "__main__":
    test_soal_1()