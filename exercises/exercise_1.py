# Your solution to Exercise 1

output = ""

alex_age = int(input())
tatyana_age = int(input())

if alex_age > tatyana_age:
	output = "Alex is the eldest."
elif tatyana_age > alex_age:
	output = "Tatyana is the eldest."
else:
	output = "Alex and Tatyana are of the same age."

print(output)