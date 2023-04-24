"""
User enters weight in pounds. App computes order price,
discount, at 3% when order price is above 100$,
tax at 8%, and shipping cost.
Shipping rate is 10 cents per pound up to and including 5 pounds,
15 cents upto and including 10 pounds, and 20 cents above that.
unit price is 15$ per pound.
Display order price, discount, tax, shipping cost, and the billed amount.
('order price' above does not include tax and shipping cost.)
"""

def compute_order_price(wt):
    unit_price = 15.0
    price = wt * unit_price

    return price

def compute_discount(price):
    discount_rate = 0.03
    if price > 100:
        discount = price * discount_rate
    else:
        discount = 0

    return discount


#main
weight = float(input('Weight ? >>'))

# 1 output : order price          input: weight (float)

order_price = compute_order_price(weight)
#2 output : discount              input: order_price

discount = compute_discount(order_price)

#3 apply discount
order_price -= discount

#4 tax


#5 ship_rate


#ship_cost


# billed all


print(weight, order_price, discount)