name = input("Please enter your name: ")
num_pizzas = int(input("How many pizzas would you like to order, " + name + "? "))
style = input("What style of pizza would you like, " + name + "? (traditional or gourmet) ")

cheese = Cheese.selectCheese(input, name)
sauce = Sauce.selectSauce(input, name)
crust = Crust.selectCrust(input, name)

num_toppings = int(input("How many toppings would you like per pizza, " + name + "? "))

pizza = Pizza(style, cheese, sauce, crust, num_toppings)
total_cost = num_pizzas * pizza.getCost()

print("You have ordered " + str(num_pizzas) + " " + style + " pizzas with the following options:")
print("- Cheese: " + cheese.getName())
print("- Sauce: " + sauce.getName())
print("- Crust: " + crust.getName())
print("You have also requested " + str(num_toppings) + " toppings per pizza.")
print("Your total cost is $%.2f." % total_cost)
