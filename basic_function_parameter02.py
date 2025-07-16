# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum(*args):
    s = 0
    for i in args:
        for j in i:
            s+=j
    return s
print(calculate_sum([2, 4, 6, 8]))