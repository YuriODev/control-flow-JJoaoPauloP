# Your solution to Exercise 3

output = ""

number = int(input("Enter a number from 0 to 36"))

even = number % 2 == 0

if number == 0:
	output = "Green"
elif number >= 1 and number <= 10:
	if even:
		output = "Black"
	else:
		output = "Red"
elif number >= 11 and number <= 18:
	if even:
		output = "Red"
	else:
		output = "Black"
elif number >= 19 and number <= 28:
	if even:
		output = "Black"
	else:
		output = "Red"
elif number >= 29 and number <= 36:
	if even:
		output = "Red"
	else:
		output = "Black"
else:
	output = "The bet will not play!"

print(output)
		