#Sals shipping calculator
weight = 8.5
ground_price = 0.0
drone_price = 0.0
ground_flat_charge = 20.00
ground_premium_charge = 125.00

print("Premium shipping is a flat rate of: " + str(ground_premium_charge))
print("Package weight is: " + str(weight) + " lbs")
#Ground Shipping
if weight <= 2:
  ground_price = 1.50 * weight + ground_flat_charge
  ground_price = round(ground_price, 2)
elif weight > 2 and weight <= 6:
  ground_price = 3.00 * weight + ground_flat_charge
  ground_price = round(ground_price, 2)
elif weight > 6 and weight <= 10:
  ground_price = 4.00 * weight + ground_flat_charge
  ground_price = round(ground_price, 2)
elif weight > 10:
  ground_price = 4.75 * weight + ground_flat_charge
  ground_price = round(ground_price, 2)
else:
  print('error')

print("Ground shipping cost: " + str(ground_price))

  #Drone Shipping
if weight <= 2:
  drone_price = 4.50 * weight
  drone_price = round(drone_price, 2) 
elif weight > 2 and weight <= 6:
  drone_price = 9.00 * weight 
  drone_price = round(drone_price, 2)
elif weight > 6 and weight <= 10:
  drone_price = 12.00 * weight
  drone_price = round(drone_price, 2) 
elif weight > 10:
  drone_price = 14.25 * weight 
  drone_price = round(drone_price, 2)

print("Drone shipping cost: " + str(drone_price))

#Find lowest price
'''
if ground_price > ground_premium_charge:
  print("Premium ")
if ground_price < drone_price and ground price < ground_premium_charge:
  print("Ground shipping is the cheapest option!")
elif ground_price > drone_price 
