# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(*args):
    a = 0
    for i in args:
        for j in i:
            if a == 0:
                a=j
            elif j<a:
                a=j
    return a
print(find_smallest([5, 2, 9, 1, 7]))