""" DIY
user enters weight in pounds.
shipping rate is 10 cents per pound upto and including 5 pounds.
shipping rate is 15 cents per pound for weight upto and including  10 pounds,
and 20 cents for all others.

display shipping cost.

"""



def shipping_rate(lbs):
    if lbs <= 5.0:
        rate = .10
    elif lbs <= 10:
        rate = .15
    else:
        rate = 0.20
    return rate


def shipping_cost(lbs, rate):
    cost = lbs * rate
    return cost

#input

weight = float(input('Enter weights in pounds >>'))
rate = shipping_rate(lbs)


#computation
shipping_cost = shipping_rate(rate) * weight


#output
print(shipping_cost)


