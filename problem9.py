# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            if i*i+j*j == k*k:
                # print("triplet found it is :", i, j, k)
                if (i+j+k) == 1000:
                    print("triplet found it is :", i, j, k)
