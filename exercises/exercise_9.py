# Your solution to Exercise 9

integer = int(input())

first_digit = integer // 100
second_digit = integer // 10 % 10
third_digit = integer % 10

if (first_digit + third_digit) < second_digit:
	print("<")
elif (first_digit + third_digit) > second_digit:
	print(">")
else:
	print("=")