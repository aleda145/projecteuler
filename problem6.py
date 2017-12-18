# Find the difference between the sum
# of the squares of the first one hundred natural numbers and the square of the sum.

x = 0
y = 0

for i in range(1, 101):
    x += i*i
    y += i

y = y*y
print("sum of squares", x)
print("square of sum", y)
print("difference", y-x)
