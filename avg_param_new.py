# Write a function which takes any number of parameters and returns their average.
parameters = [1, 10, 4, 5, 8, 9]


def average(args: list):
    return sum(args) / float(len(args))


print(average(parameters))
