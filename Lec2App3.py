""" DIY
user enters weight in pounds.
shipping rate is 10 cents per pound upto and including 5 pounds.
shipping rate is 15 cents per pound for weight upto and including  10 pounds,
and 20 cents for all others.

display shipping cost.

"""



def compute_shipping_rate(lbs):
    if lbs <= 5.0:
        rate = .10
    elif lbs <= 10:
        rate = .15
    else:
        rate = 0.20
    return rate


def compute_shipping_cost(lbs, rt):
    cost = lbs * rt
    return cost

#input

weight = float(input('Enter weights in pounds >>'))


#computation
rate = compute_shipping_rate(weight)
shipping_cost = compute_shipping_cost(weight,rate)


#output
print(shipping_cost)


