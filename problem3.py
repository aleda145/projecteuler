# What is the largest prime factor of the number 600851475143 ?


def find_prime_factors(number):
    # this range is obviously bad, there is no reason to check if divisible by  4, 6, 8, 9, 10 etc.
    for x in range(2, number+1):
        if number % x == 0:
            print("divisible with ", x)
            if number/x == 1:
                return x
            else:
                # make the new number into an int because python is not strongly typed
                new_number = int(number/x)
                print("new number", new_number)
                return find_prime_factors(new_number)


print("largest prime factor is:", find_prime_factors(600851475143))
