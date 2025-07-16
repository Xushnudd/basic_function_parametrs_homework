# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculated_average(*args):
    a = 0
    b = 0
    for i in args:
        for j in i:
            a+=j
            b+=1
    return int(a/b)
print(calculated_average([85, 90, 92, 88, 95]))
print(calculated_average([12, 10, 20, 15, 18]))