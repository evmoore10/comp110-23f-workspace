"""Defining a class!"""

from __future__ import annotations
"""
Thimk of a class definition as a roadmap for bojects belonging to the class
Defining the underlyning structure every instance of this class will have
"""


class Pizza:
    """Class to represnt pizza!"""
 
    # attributes
    # syntax name : type
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        """Constuctor"""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        # returns self

# defining method
    def price(self) -> float:
        """Method to compute price of pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    

    def add_toppings(self, num_toppings: int):
        """Update existing pizza order with num_toppings"""
        self.toppings += num_toppings

    
    def add_toppings_new_order(self, num_toppings: int) -> Pizza:
        """Make new pizza order using existing info"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    
    def __str__(self) -> str:
        """Result when I call str()"""
        return "This is a pizza!"
    
my_pizza: Pizza = Pizza("medium", 3, False)
print(str(my_pizza))
sals_pizza: Pizza = Pizza("large", 3, True)
print(str(sals_pizza))