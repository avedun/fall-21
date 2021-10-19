#divosors

#Create a program that asks the user for a number and then prints out a
# list of all the divisors of that number. (If you don’t know what a divisor is,
# it is a number that divides evenly into another number. For example, 13 is a
# divisor of 26 because 26 / 13 has no remainder.)

print('This program will find divisors of the user\'s input.')
num = int(input('input a number: '))

num_range = list(range(1, num + 1))

print(num_range)

k = 0
j = 1
i = 0
#for i in num_range:
while i < max(num_range):
    if num % num_range[i] == 0:
        print(num_range[i])
        #print('{1} is a divisor of {0} because {0} / {1} has no remainder'.format(num, num_range[i]))
    i += 1

# OR
print('OR')
for i in num_range:
    if num % i == 0:
        print(i)
#while i < max(num_range)