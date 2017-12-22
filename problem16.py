# 2^15 = 32768 sum of digits = 3 + 2 + 7 + 6 + 8 = 26

# sum of digits in 2^1000?
import math

two_to_1000 = int((math.pow(2,1000)))
print(two_to_1000)
two_to_1000_str = str(two_to_1000)
print(two_to_1000_str)
sum_of_digits = 0
for i in range(0, len(two_to_1000_str)):
    print(two_to_1000_str[i])
    sum_of_digits += int(two_to_1000_str[i])

print(sum_of_digits)