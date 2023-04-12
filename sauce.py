def get_name(self):
    return self.name

def get_cost(self):
    return self.cost

@staticmethod
def select_sauce(input, name):
    print("What type of sauce would you like, " + name + "? (marinara, PlumTomato, Barbecue, or Pumpkin) ")
    sauce_name = input.nextLine()
    sauce_name = sauce_name.lower()
    if sauce_name == "plumtomato":
        return Sauce("PlumTomato", 1.99)
    elif sauce_name == "barbecue":
        return Sauce("Barbecue", 1.58)
    elif sauce_name == "pumpkin":
        return Sauce("Pumpkin", 1.16)
    else:
        return Sauce("Marinara", 0.00)
