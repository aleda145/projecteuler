# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def check_if_x_digit_palindrome(number):
    num_string = str(number)
    num_correct = 0
    x = int(len(num_string)/2)
    for i in range(0, x):
        if num_string[0+i] == num_string[len(num_string)-1-i]:
            num_correct += 1
    if num_correct == x:
        return True

largest_palindrome = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if check_if_x_digit_palindrome(i*j):
            if i*j > largest_palindrome:
                largest_palindrome = i*j

print(largest_palindrome)
