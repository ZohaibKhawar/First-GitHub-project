import coffee_shop


print("Welcome to", coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available roasts:", coffee_shop.coffee_roasts)

order_size = input("What size coffee do you want? ")
order_roast = input("What roast do you want? ")
shop_says = coffee_shop.order_coffee(order_size, order_roast)
print(shop_says)

add_milk_response = input("Do you want to add milk (y/n)? ")
if "y" in add_milk_response.lower():
    milk_fat = input("What percent milk do you want added? ")
    shop_says = coffee_shop.add_milk_please(milk_fat)
    print(shop_says)

add_donut_response = input("would you like a donut (y/n)? ")
if "y" in add_donut_response.lower():
        donut_sprinkles = input("would you like a donut with sprinkles (y/n)?")
        if "y" in donut_sprinkles.lower():
            shop_says = coffee_shop.add_donut_please(donut_sprinkles)
            print(shop_says)


print("THAT'S GOOD COFFEE!  Very good.  Your brain is working again.")
print("You better give a tip.")
tip_amount = input("Tip amount? ")
coffee_shop.give_tip(tip_amount)