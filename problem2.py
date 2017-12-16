# By considering the terms in the Fibonacci sequence whose values do not exceed four million
# find the sum of the even-valued terms.


def fibonacci(n1, n2, fibo_sum):
    n3 = n1+n2
    if n3 % 2 == 0:
        fibo_sum += n3
        print("sum so far", fibo_sum)

    if n3 < 4000000:
        print("fibo term:", n3)
        return fibonacci(n2, n3, fibo_sum)
    else:
        return fibo_sum

print("answer is:", fibonacci(1, 2, 2))