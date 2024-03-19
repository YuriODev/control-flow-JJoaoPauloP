# Your solution to Exercise 13

four_digit_number = int(input())

first_digit = four_digit_number // 1000
second_digit = four_digit_number // 100 % 10
third_digit = four_digit_number // 10 % 10
fourth_digit = four_digit_number % 10 

if first_digit != second_digit != third_digit != fourth_digit:
	print("True")
else:
	print("False")