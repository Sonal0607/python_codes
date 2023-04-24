#1 
""" users enter income:
tax rate is 10% for income upto and including
100,000.00
otherwise 15%
compute display tax.

input : (float)
output(float)"""

#function

def compute_tax_rate(inc):
    if inc <= 100000.0:
        rate = 0.1
    else:
        rate = 0.15

    return rate

def compute_tax(inc, tr):
    tax = inc * tr
    return tax



#main
#inputs
income = float(input('Income >>'))

#computations
#1. compute the tax rate out: tax_rate float in: float
tax_rate = compute_tax_rate(income)

#2. compute tax out: tax float in: tax_rate flaots
tax = compute_tax(income, tax_rate)

#outputs

print(income, tax_rate)