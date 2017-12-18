# What is the 10 001st prime number?
# a brute force would take a lot of time here!
# using sieve of Eratosthenes
# https://www.wikiwand.com/en/Sieve_of_Eratosthenes

# Boolean array

VERY_BIG_NUMBER = 1000000

primes = [True for i in range(VERY_BIG_NUMBER)]
p = 2
print ("generated array")

while p * p <= VERY_BIG_NUMBER:
    if primes[p]:
        for j in range(p*p, VERY_BIG_NUMBER, p):
            primes[j] = False
    p += 1

#print(primes)

counter = 0
for i in range(VERY_BIG_NUMBER):
    if primes[i]:
        #print(i)
        counter += 1
        # add +2 to counter because 1 and 0 are not technically primes.
        if counter == 10003:
            print("10001st prime:", i)
            break
print("largest found was number:", counter)
