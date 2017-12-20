# Find the sum of all the primes below two million.


# reusing code from problem 7
VERY_BIG_NUMBER = 2000000

primes = [True for i in range(VERY_BIG_NUMBER)]
p = 2
print ("generated array")

while p * p <= VERY_BIG_NUMBER:
    if primes[p]:
        for j in range(p*p, VERY_BIG_NUMBER, p):
            primes[j] = False
    p += 1

prime_sum = 0
for i in range(VERY_BIG_NUMBER):
    if primes[i]:
        # print(i)
        prime_sum += i


# -1 because 1 is not a prime number
print("the sum is:", prime_sum-1)
