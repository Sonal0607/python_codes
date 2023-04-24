#Lec1App1.py

#user enters name , age and income.tax rate is 15%. display tax.
#inputs: income, age, income
#outputs: tax


""" Lecture 1 App 1. Developed by Manoj. 04/12/2023.

A tax computation app.
inuts: name (str) age (int) income (flaot)
outputs : tax(float)
"""


#inputs
name = input('Enter your name >')
age = int(input('How old are you ?\n>'))
income = float(input('Enter your income >'))

#initialisations
tax_rate = 0.15

#computations
tax = income * tax_rate


#outputs
print(f'Hello: {name:s}! \n You are {age:d} years old.\nIncome:\t{income:.2f} \n Tax:\t {tax:.2f}')  #informative, formatted
#float f int d str s
#\t tab \n newline
#something () a funtion

#notes
# how do we represent the data ?
# variables? inputs? outputs? any other ?
# solve the problem. code it. verify it. document it.




#strings intergers real numbers
#str int float
#'hello'


#AVOID
#print(income * tax_rate)
#tax = income * 0.15