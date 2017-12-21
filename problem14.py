# Longest Collatz sequence
# brute force solution, possibly make a dictionary to make it faster?


def collatz_sequence(number, collatz_list):
    collatz_list.append(number)

    if number == 1:
        return
    if number % 2 == 0:
        collatz_sequence(int(number/2), collatz_list)
    elif number % 2 == 1 and number != 1:
        collatz_sequence(int(3*number+1), collatz_list)

    return collatz_list


c_list = []

x = collatz_sequence(14, c_list)

largest_chain = 0
largest_number = 0
print(len(x))

for i in range(2, 1000000):
    c_list = []
    x = collatz_sequence(i, c_list)
    if len(x) > largest_chain:
        largest_chain = len(x)
        largest_number = x

print(largest_chain)
print(largest_number)