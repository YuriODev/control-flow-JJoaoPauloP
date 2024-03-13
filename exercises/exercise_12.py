# Your solution to Exercise 12

four_digit_number = int(input())

output = ""

fourth_digit = four_digit_number % 10
third_digit = four_digit_number // 10 % 10
second_digit = four_digit_number // 100 % 10
first_digit = four_digit_number // 1000

if fourth_digit % 2 == 0:
	fourth_digit = "*"
if third_digit % 2 == 0:
	third_digit = "*"
if second_digit % 2 == 0:
	second_digit = "*"
if first_digit % 2 == 0:
	first_digit = "*"

output = str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit)

print(output)