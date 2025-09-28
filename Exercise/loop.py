"""Create program for:
1. print number 1 to 20,
2. Skip number which divisible by 3,
3. Stop loop if number was more than 15. """

for i in range(1, 21):
    if i % 3 == 0:
        continue
    if i >= 15:
        break
    print(i)

print("-----------------------------------------------------------------------")

"""Buat program yang menampilkan pola segitiga bintang seperti ini:
*
**
***
****
*****
"""

for i in range(1, 6):
    print(i*"*")