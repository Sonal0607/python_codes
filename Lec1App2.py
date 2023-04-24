#Lecture 1 App 2


#input : income :
#tax rate is 10% below 100,000 20% otherwise.
#display tax

""" #inputs
income = float(input('Income :'))

#computations
# 1. find the tax rate out : tax_rate
if income < 100000.0:
    tax_rate = 0.1
else:
    tax_rate : 0.2

#end if


# 2. compute the tax. out : tax
tax = income * tax_rate


#output 
print(income, tax)
"""



# < > <= >=
# if score ==100: 'double equals'
# if score != 0: 'not equals'


#input : weight.
#ship rate : 50 cents per pound, for weight upto and including 5 pounds. 75 cents per pound otherwise.
'''
weight = float(input('Weight(lb) >'))

#ship_rate

if weight <= 5.0:
    ship_rate = 0.50
else:
    ship_rate = 0.75
#end if


shipping_cost = weight * ship_rate

print(shipping cost)

'''

#score (interger) is the input. assume range 0..100
#grade A or B. >= 80 is A. else B. Display grade.
#80- 100 A
# 60- 79 B
# 40 -59 C
# 0-39 D


#input: score(int)
#output: ( str)
""" 
score = int(input('Enter you score >> '))

if score >= 80:      # 80-100
    grade = 'A'
elif score >= 60:     # you know the score < 80
   grade =  'B'
elif score >= 40:    # you know the score  < 60
    grade = 'C'
else:
    grade = 'D'

#collectiviely exhaustive


print(score,grade)
 """

'''
order_price = 1000.0
discount_rate = 0.03

#if price is above 100$ a discount of 3% is given.
#display discount and final price.


if order_price > 100:
    discount = order_price * discount_rate
else:
    discount = 0.0


order_price = order_price - discount
#order_price -= discount 

print(order_price, discount)

#if a variable gets its value inside an if statement, 
# ensure that it has a value under every possibility.

'''

# student can be on a credit basis (grade A or B) or 
# audit basis (grade Pass or Fail)

#user enters grade basis, or not,
# and the score (integer)

# grade basis : >= 80 A others get B
# audit > 40 pass other Fail.
#Display the grades A/B?Pass/Fail.

score = int(input(' Score ? '))

graded = int(input('Enter 1 for credit basis, 0 for audit basis >>'))

# 'nested if'

if graded:

    # >= 80 A others get a B
    if score >= 80:
        grade = 'A'
    else:
        grade = 'B'
else:
    # > 40 Pass other Fails
    if score > 40:
        grade = 'Pass'
    else:
        grade = 'Fail'

print( score, graded, grade)


# 1 True 0 False. The int type also serves as the bool.

# use the nested if instead of using and,

# if daytime:
# if raining 
# let us code



# if day time and raining:
# let us code.

# instead of the OR use if ... elif...

# if a == 10 or b ==20:
# x = 100

# if a == 10:
# x = 100

# if b == 20:
# x = 100




