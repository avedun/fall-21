'''
=============================
Lab 1 Amortization Calculator
=============================

:Description: This script implements the amortization formula which can
              be used to find the monthly mortgage payment for a fixed rate
              mortgage of a home at an annual interest rate. The user inputs
              the principal, the interest rate, and number of years.

:Author:      Prof. Widulski
:Date:        9/10/2021
:Class:       Computer Programming 1
:Lab:         Propositional Logic
:Version:     1.0
:Inputs:      principal - The principal amount of the loan.
              annual_rate - The annual interest rate as a percent.
              years - The number of years of the loan.
:Output:      monthly_payment - The amount you need to pay every month.
:Misc. Vars:  num_payments - The total number of payments for the life of
                             the loan (12 * years).
              monthly_rate - The monthly interest rate as a decimal.
                             (i.e., annual_rate / 1200)
'''
# GOOD STYLE: Display to the user the purpose of the program before the input section
print('This progam calculates the monthly payment for a fixed-rate mortgage')
print('using an amortization calculator. In order to do this, we will need ')
print('the principal, annual interest rate, and the term (years) of the loan.')

# INPUT SECTION
# TODO: Input the three input variables listed in the comments (program analysis) above.
principal = int(input('Please enter the principal: '))
annual_rate = float(input('Please enter the interest rate (APR): '))
years = int(input('Please enter the term of the loan (i.e., the number of years): '))
# Note the principal and interest rate are floats while years is an integers.


# PROCESSING SECTION
num_payments = years * 12;
monthly_rate = annual_rate / 1200;
# TODO: Write the annuity formula on the instructions in Python using the appropriate variables.

monthly_payment = principal * (monthly_rate + ((monthly_rate / (((1 + monthly_rate) ** num_payments) - 1))))
# OUTPUT SECTION

print()
print('Your monthly payment will be: ${:,.2f}'.format(monthly_payment))
