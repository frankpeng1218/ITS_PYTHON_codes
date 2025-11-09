numbers = [21, 4, 35, 1, 8, 7, 3, 6, 9]
odd_numbers = []
for number in numbers:
    if (number % 2 != 0): #將奇數放入 odd_numbers 串列
        odd_numbers.append(number)
print(odd_numbers)