

'''Homework 1 App 1.   Developed by : Sonal Mann. 18 April 2023.

Cost computation App.
input : weights (int)
outputs : cost (float), shipping charges (float) and total cost (float) '''


#user enters weights for each product. display cost , shipping charges & total cost.



#inputs
artichokes_weight = int(input('Enter order in pounds for artichokes \n >'))
carrots_weight = int(input('Enter order in pounds for carrots \n >'))
beets_weight = int(input('Enter order in pounds for beets \n >'))



#initialisations
artichokes_price_per_pound = 2.67
carrots_price_per_pound = 1.49
beets_price_per_pound = 0.67
discount_rate = 0.05


#computation
cost = artichokes_weight * artichokes_price_per_pound + carrots_weight * carrots_price_per_pound + beets_weight * beets_price_per_pound
total_weight = artichokes_weight + carrots_weight + beets_weight

#discount applied before shipping charges
if cost > 100:     # total order cost above $100 
    discount = cost * discount_rate
else:              
    discount = 0
#ends if

cost = cost - discount   #cost after applying discount



#shipping_rate
if total_weight <= 5:           # weight less than or equals to 5 pounds
    shipping_charges = 3.50
elif total_weight <= 20:        # weight less than or equals to 20 pounds
    shipping_charges = 4.00
else:
    shipping_charges = 9.50 + (0.10 * total_weight)      # weight more than 20 pounds
#ends if

total_cost = cost + shipping_charges #total cost after applying any discounts and shipping cost


#Output
print(f'Cost : ${cost: .2f}\n Shipping charges : ${shipping_charges: .2f} \n Total cost : ${total_cost : .2f}')