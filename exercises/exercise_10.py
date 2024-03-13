# Your solution to Exercise 10

x1 = int(input())
x2 = int(input())
x3 = int(input())
y1 = int(input())
y2 = int(input())
y3 = int(input())

pythagorean_theorem = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
absolute_length_AC = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

if pythagorean_theorem == absolute_length_AC:
	print("Yes")
else:
	print("No")
