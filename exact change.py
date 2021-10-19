# Write a program with total change amount as an integer input,
# and output the change using the fewest coins, one coin type per line.
# The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies.
# Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

coins = {100: 'Dollar', 25: 'Quarter', 10: 'Dime', 5: 'Nickel', 1: 'Penny'}

coin_input = int(input())
left = coin_input

if coin_input <= 0:
    print('No change')
else:
    for i in coins:
        if (left / i >= 1):
            temp = left // i
            left = left - (temp * i)
            print(temp,'', end='')
            if (temp == 1):
                print(coins[i])
            elif ((i == 1) and temp < 4):
                print('pennies')
            elif (temp > 1):
                print(coins[i], 's', sep='')

