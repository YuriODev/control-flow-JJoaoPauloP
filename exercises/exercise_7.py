# Your solution to Exercise 7

first_number = float(input())
second_number = float(input())
arithmetic_operation = input()

if arithmetic_operation == "+":
	print(first_number + second_number)
elif arithmetic_operation == "-":
	print(first_number - second_number)
elif arithmetic_operation == "*":
	print(first_number * second_number)
elif arithmetic_operation == "mod":
	print(first_number % second_number)
elif arithmetic_operation == "pow":
	print(first_number ** second_number)
elif arithmetic_operation == "/" or arithmetic_operation == "mod":
	if second_number == 0:
		print("Division by 0!")
	elif arithmetic_operation == "/":
		print(first_number / second_number)
	else:
		print(first_number % second_number)