# Your solution to Exercise 2

output = ""
age = int(input())

if age <= 1:
	output = "You are an infant."
elif age < 13:
	output = "You are a child."
elif age < 20:
	output = "You are a teenager."
else:
	output = "You are an adult."

print(output)