# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
# any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
x = 0
while True:
    x += 20
    y = 0
    for i in range(1, 21):
        if x % i == 0:
            # print(x, "was divisible with:  ", i)
            y += 1
        else:
            break
    if y == 20:

        print(x)
        break

# very badly optimized solution.
