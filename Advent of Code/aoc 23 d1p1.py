
import re


file_path = "C:\\Users\\TUFFTHYMEZ\\Desktop\\Python\\aoc 23 d1 output.txt"

numbers_list = []
with open(file_path, "r") as file:
    for line in file:
        # Erste Zahl in der Zeile finden
        first_number = re.search(r'\d', line)
        if first_number:
            first_number = int(first_number.group())
        else:
            first_number = None
        last_numbers = re.findall(r'\d', line)
        if last_numbers:
            last_number = int(last_numbers[-1])
        else:
            last_number = None

        numbers_list.append((first_number, last_number))
merg_F = []
add_L = []
total = []
for idx, (first, last) in enumerate(numbers_list, start=1):
    merg_F.append(first)
    add_L.append(last)
    

print("first : ", sum(merg_F), "last : ", sum(add_L))
# !!! first mal 10 nicht vergessen + last !!!