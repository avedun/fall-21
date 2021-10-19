# Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

#Extras:

# Instead of printing the elements one by one, make a new list that has all the elements
# less than 5 from this list in it and print out this new list.

# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original
# list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for nums in a: # estabilish 'nums'
    if nums < 5: # determine if 'nums' is less than 5
        print(nums) # print 'nums' if it is less than 5

range(1,5) # 'range' numbers from 1 up to, but befor 5, so 1, 2, 3, and 4.
list(range(1,5)) # list(range) converts range to a list
c = list(range(1,5)) # assign out list(range) to a variable
print(c) # [1, 2, 3, 4]

for i in range(1,5):
    print(i)

