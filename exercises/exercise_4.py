# Your solution to Exercise 4

output = ""
grade = int(input("Enter grade:"))

if grade >= 1 and grade <= 3:
	output = "initial level"
elif grade <= 6:
	output = "average level"
elif grade <= 9:
	output = "sufficient level"
elif grade <= 12:
	output = "high level"
else:
	output = "level is absent"

print(output)