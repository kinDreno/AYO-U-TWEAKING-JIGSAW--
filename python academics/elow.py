x = int(input("input first n: "))
y = int(input("input second n:"))
R = 0
d = x - y

if (d < 0):
    R += x + y
elif (d == 0):
    R += (2 * x) + (2 * y)
else:
    R += x * y

print(f"X value {x}, Y value: {y}. \n The result of R: {R}")