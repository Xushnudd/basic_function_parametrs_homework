# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(*args):
    s = 0
    for i in args:
        a = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for j in a:
           for b in range(len(i)):
               if i[b] == j:
                   s+=1
    return s
print(count_vowels("hello_world"))