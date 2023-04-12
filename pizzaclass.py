def getCost(self):
    cost = 5.00  # base cost of pizza
    
    if self.style.lower() == "gourmet":
        cost += 2.00  # additional cost for gourmet style
    
    cost += self.cheese.getCost() + self.sauce.getCost() + self.crust.getCost()
    cost += self.num_toppings * 0.50  # additional cost per topping
    
    return cost
