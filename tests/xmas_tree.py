# create a function that takes a heigh as a parameter and prints out a Christmas tree using *

# height = 4

 #    *
 #   ***
 #  *****
 # *******
 #    |


def print_christmas_tree(height):
    for k in range(height):   # range goes from zero up to (but not including) height value
        print(" " * (height - 1 - k) + "*" *(1 + 2*k))

    print(" " * (height-1) + "|")

     # OR

    print("|".rjust(height, ' '))


print_christmas_tree(12)