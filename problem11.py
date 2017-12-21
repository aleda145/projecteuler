# EXTREMELY UGLY SOLUTION!


number_grid = "0802229738150040007504050778521250779108"\
              "4949994017811857608717409843694804566200"\
              "8149317355791429937140675388300349133665"\
              "5270952304601142692468560132567137023691"\
              "2231167151676389419236542240402866331380"\
              "2447326099034502447533537836842035171250"\
              "3298812864236710263840675954706618386470"\
              "6726206802621220956394396308409166499421"\
              "2455580566739926971778789683148834896372"\
              "2136230975007644204535140061339734313395"\
              "7817532822753167159403800462161409535692"\
              "1639054296353147555888240017542436298557"\
              "8656004835718907054444374460215851541758"\
              "1980816805944769287392138652177704895540"\
              "0452088397359916079757321626267933279866"\
              "8836688757622072034633674655123263935369"\
              "0442167338253911249472180846293240627636"\
              "2069364172302388346299698267598574043616"\
              "2073352978319001743149714886811623570554"\
              "0170547183515469169233486143520189196748"\

print(number_grid)
number_array = []

for j in range(0, 800, 2):
    str = number_grid[j]+number_grid[j+1]
    number_array.append(int(str))
    # print("coords:", j, "and string:", str)

print(number_array)
# vertical
greatest_product= 0
for j in range(0, 20):
    print("column: ", j)
    for i in range(0+j, 340, 20):

        print("product of", number_array[i], number_array[i+20], number_array[i+40],
              number_array[i+60])
        product = number_array[i] * number_array[i+20] * number_array[i+40] * number_array[i+60]
        print(product)
        if product > greatest_product:
            greatest_product = product
            print("new greatest product: ", greatest_product)

    print("greatest product was: ", greatest_product)

# diagonel top left to bottom right
# dont go further than column 16 because they wont be valid solutions.
for j in range(0, 17):
    print("column: ", j)
    for i in range(0+j, 340, 20):
        print("product of", number_array[i], number_array[i + 21], number_array[i + 42],
              number_array[i + 63])
        product = number_array[i] * number_array[i + 21] * number_array[i + 42] * \
            number_array[i + 63]
        print(product)

        if product > greatest_product:
            greatest_product = product
            print("new greatest product: ", greatest_product)

    print("greatest product was: ", greatest_product)

# diagonal bottom right to top left
for j in range(0, 17):
    print("column: ", j)
    for i in range(399-j, 60, -20):
        print("product of", number_array[i], number_array[i - 21], number_array[i - 42],
              number_array[i - 63])
        product = number_array[i] * number_array[i - 21] * number_array[i - 42] * \
            number_array[i - 63]
        print(product)
        if product > greatest_product:
            greatest_product = product
            print("new greatest product: ", greatest_product)
    print("greatest product was: ", greatest_product)

# diagonal top right to bottom left
for j in range(20, 3, -1):
    print("column: ", j)
    for i in range(19-j, 340, 19):
        print("product of", number_array[i], number_array[i + 19], number_array[i + 38],
              number_array[i + 57])
        product = number_array[i] * number_array[i + 19] * number_array[i + 38] * \
            number_array[i + 57]
        print(product)
        if product > greatest_product:
            greatest_product = product
            print("new greatest product: ", greatest_product)
    print("greatest product was: ", greatest_product)

# left to right
for j in range(0, 17):
    print("column: ", j)
    for i in range(0 + j, 400, 20):
        print("product of", number_array[i], number_array[i + 1], number_array[i + 2],
              number_array[i + 3])
        product = number_array[i] * number_array[i + 1] * number_array[i + 2] * \
            number_array[i + 3]
        print(product)
        if product > greatest_product:
            greatest_product = product
            print("new greatest product: ", greatest_product)

print("greatest product was: ", greatest_product)