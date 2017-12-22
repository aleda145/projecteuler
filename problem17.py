one = 'one'
two = 'two'
three = 'three'
four = 'four'
five = 'five'
six = 'six'
seven = 'seven'
eight = 'eight'
nine = 'nine'
list_of_singles = ["", one, two, three, four, five, six, seven, eight, nine]
print (list_of_singles)
# the teens and ten are special cases, dont need to care about them
ten = 'ten'
eleven = 'eleven'
twelve = 'twelve'
thirteen = 'thirteen'
fourteen = 'fourteen'
fifteen = 'fifteen'
sixteen = 'sixteen'
seventeen = 'seventeen'
eighteen = 'eighteen'
nineteen = 'nineteen'
list_of_teens = [ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen,
                 nineteen]

twenty = 'twenty'
thirty = 'thirty'
forty = 'forty'
fifty = 'fifty'
sixty = 'sixty'
seventy = 'seventy'
eighty = 'eighty'
ninety = 'ninety'
list_of_doubles = ["", "", twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety]
hundred = 'hundred'
list_of_triples = ["", one+hundred +"and", two+hundred+"and", three+hundred+"and",
                   four+hundred+"and", five+hundred+"and", six+hundred+"and",
                   seven+hundred+"and", eight+hundred+"and", nine+hundred+"and"]

char_counter = 0
for h in range(0, 10):
    for i in range(0, 10):

        for j in range(0, 10):
            if i == 0 and j == 0:
                new_string = list_of_triples[h][:-3]
                char_counter += len(new_string)
                print(new_string)
            elif i == 1:
                new_string = list_of_triples[h]+list_of_teens[j]
                print(new_string)
                char_counter += len(new_string)
            else:
                new_string = list_of_triples[h]+list_of_doubles[i]+list_of_singles[j]
                print(new_string)
                char_counter += len(new_string)

#one thousand = 11 char
print(char_counter+11)