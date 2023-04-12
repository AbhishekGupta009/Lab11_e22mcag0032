def getName(self):
    return self.name

def getCost(self):
    return self.cost

@staticmethod
def selectCheese(input, name):
    print(f"What type of cheese would you like, {name}? (mozzarella, Provolone, Reggiano, or Parmesan) ")
    cheese_name = input.nextLine()
    cheese_name = cheese_name.lower()
    if cheese_name == "reggiano":
        return Cheese("Reggiano", 1.99)
    elif cheese_name == "provolone":
        return Cheese("Provolone", 1.58)
    elif cheese_name == "parmesan":
        return Cheese("Parmesan", -0.99)
    else:
        return Cheese("Mozzarella", 0.00)
