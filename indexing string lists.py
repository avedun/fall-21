# reverse indexing lists

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# METHOD ONE:

input = input()
max = len(input) - 1
check = ''
k = 0

for i in input:

   #if input[input.index(i)] == input[max - k]:             ALL
       #check += input[input.index(i)]                      OF

   #if input[0 + k] == input[-len(input) + k]:              THESE
       #check += input[k]                                   WORK

   if input[0 + k] == input[max - k]:
       check += input[k]
       k += 1
       if check == input:
           print('palindrome')

if check != input:
    print('not')

# METHOD TWO:
# only needs 'input' variable

if input[::-1].lower() == input.lower(): # ::-1 goes from the last element backwords. reverse elements
    print('p')                           # 'string'.lower() also converts to lowercase 
else:
    print('not')
print() # enter
print(input[:len(input)]) # print element from element 0 of 'input' to the element at the element length of 'input'