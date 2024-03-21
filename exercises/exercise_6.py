# Your solution to Exercise 6

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

output = ""

distance_from_originA = ((x1**2) + (y1**2))**0.5
distance_from_originB = ((x2**2) + (y2**2))**0.5

if distance_from_originA < distance_from_originB:
	output = "B is further from the origin."
elif distance_from_originA > distance_from_originB:
	output = "A is further from the origin."
else:
	output = "A and B are at the same distance from the origin."

print(output)