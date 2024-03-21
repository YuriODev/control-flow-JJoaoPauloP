# Your solution to Exercise 5

a = float(input())
b = float(input())
c = float(input())
		  
discriminant = b**2 - 4*a*c
quadratic = False
linear = False

if a != 0.0:
	quadratic = True

if quadratic:
	if discriminant < 0:
		print("No roots.")
	elif discriminant == 0:
		print((-b+(discriminant)**1/2) /2*a)
	elif discriminant > 0:
		output = (-b+(discriminant)**1/2) /2*a
		output2 = (-b-(discriminant)**1/2) /2*a
		print(output, "and", output2)

if not quadratic and b != 0.0:
	linear = True

if linear:
	print(c/b)

if not linear and not quadratic:
	if a == b == c == 0:
		print("Infinite roots.")
	else:
		print("No roots.")