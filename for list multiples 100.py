# compute all multiples of 3 and 5
# that are less than 100
# find the sum of those numbers

list = range(1, 100)
newlist = []

for i in list:
    if i % 3 == 0 or i % 5 == 0:
        newlist.append(i)
print(sum(newlist))

print('{x:.2f} hello'.format('x' == 5.4232))
