# Your solution to Exercise 11

year = int(input())

if year % 4 == 0:
	if year % 100 != 0 or year % 400 == 0:
		print("Leap year.")
	else:
		print("Ordinary year.")
else:
	print("Ordinary year.")