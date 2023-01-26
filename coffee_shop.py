shop_name = "Runestone Brew House"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]

def order_coffee(size, roast):
    return "Here's your {} coffee roasted {}".format(size, roast)

def add_milk_please(fat_content):
    return "I've added the {}% milk".format(fat_content)

def add_donut_please(donut_sprinkles):
    return "Here is your donut".format(donut_sprinkles)

def give_tip(tip_amount):
    print("Thank you so much!  We don't make a ton of money.")


