# What is the value of the first triangle number to have over five hundred divisors?

# Brute force solution that was too slow
# z = 0
# i = 0
# number_of_divisors = 0
# greatest_number_of_divisor = 0
# while True:
#     i += 1
#     z += i
#     # print(z)
#     number_of_divisors = 0
#     for j in range (1, z+1):
#         if z % j == 0:
#             # print("divisible by: ", j)
#             number_of_divisors += 1
#
#     if number_of_divisors > greatest_number_of_divisor:
#         greatest_number_of_divisor = number_of_divisors
#
#     if greatest_number_of_divisor > 500:
#         # print(greatest_number_of_divisor)
#         print("the number that has divisors over 500 is:", z)
#         break


def find_prime_factors(number, prime_list):
    # this range is obviously bad, there is no reason to check if divisible by  4, 6, 8, 9, 10 etc.
    for x in range(2, number+1):
        if number % x == 0:
            # print("divisible with ", x)
            prime_list.append(x)
            if number/x == 1:

                return prime_list
            else:
                # make the new number into an int because python is not strongly typed
                new_number = int(number/x)
                # print("new number", new_number)

                return find_prime_factors(new_number, prime_list)


def find_divisors(list_of_prime):
    # print(list_of_prime)
    x = 1
    for j in range(0, list_of_prime[-1]+1):
        # print(list_of_prime.count(j))
        if list_of_prime.count(j) != 0:
            x *= (list_of_prime.count(j)+1)
    return x


def triangular_number(n):
    return int(n*(n+1)/2)

prime_list = []
# print(triangular_number(7))

# print(find_prime_factors(triangular_number(7)))

n = 2
while True:
    prime_list = []
    z = find_prime_factors(triangular_number(n), prime_list)

    # print("number:", z)
    # print("divisors:", find_divisors(z))
    if find_divisors(z) > 500:
        print(z)
        print("number:", triangular_number(n))
        break
    n += 1