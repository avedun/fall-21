'''
==================================================
Programming Assignment 2: Roman Numerals Converter
==================================================
:Description: This program converts an inputted number between 0 and 3,999,
              inclusive, into its Roman numeral equivalent.
:Author:      Prof. Widulski
:Date:        9/10/2021
:Class:       Computer Programming 1
:Project:     Programming Assignment 2
:Version:     1.0    
:Inputs:      number - The user inputted number must be < 4000.
:Output:      roman_numeral - The string representing the number in
                              Roman numerals.
:Misc. Vars:  digit - The current digit that is being processed or converted
                      into Roman numerals.
              remaining_digits - The remaining digits that are yet to be
                                 processed.
'''
# GOOD STYLE: Display to the user the purpose of the program
# INPUT SECTION
print('This program converts a positive integer up to 3,999 into the')
print('Roman number system. Enter a positive integer:', end=' ')
number = int(input())

# PROCESSING SECTION
thou = number // 1000
hund = number % 1000 // 100
tens = number % 100 // 10
ones = number % 10

onesrn = {0 : '', 1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX'}
tensrn = {0 : '', 1 : 'X', 2 : 'XX', 3 : 'XXX', 4 : 'XL', 5 : 'L', 6 : 'LX', 7 : 'LXX', 8 : 'LXXX', 9 : 'XC'}
hundrn = {0 : '', 1 : 'C', 2 : 'CC', 3 : 'CCC', 4 : 'CD', 5 : 'D', 6 : 'DC', 7 : 'DCC', 8 : 'DCCC', 9 : 'CM'}
thourn = {0 : '', 1 : 'M', 2 : 'MM', 3 : 'MMM'}

if number >= 0 and number < 4000:
    roman_numeral = ''
    # TODO: Complete the processing of the 4 digit number
    # Get the thousands digit
    # Convert the thousands digit into Roman numerals and concatenate it with roman_numeral
    # Get the hundreds digit
    # Convert the hundreds digit into Roman numerals and concatenate it with roman_numeral
    # Get the tens digit
    # Convert the ones digit into Roman numerals and concatenate it with roman_numeral
    # Get the ones digit
    # Convert the ones digit into Roman numerals and concatenate it with roman_numeral

    roman_numeral = (thourn[thou]) + (hundrn[hund]) + (tensrn[tens]) + (onesrn[ones])
    # OUTPUT SECTION
    print()
    print('{} written in roman numerals is {}.'.format(number, roman_numeral))
else:
    print()	
    print('Invalid input!! Input must be a positive integer less than 4,000.')
