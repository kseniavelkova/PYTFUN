import math

# Create a lambda which returns the first item in a list.

letters = ['a', 'b', 'c', 'd', 'e']

first_letter = lambda x: x[0]

print(first_letter(letters))

# Map a lambda which applies the logistic function to the list [-3, -5, 1, 4] . Round each number to 4 decimal places. (ermm…. that's two nested maps)


num_list = [-3, -5, 1, 4]

new_list = list(map(lambda x: round(x, ndigits=4), list(map(lambda x: 1 / (1 + math.exp(x)), num_list))))

print(new_list)
