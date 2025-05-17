class MenuItem:
    def __init__(self, name: str    , price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price

class Drink(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size 

class Entrance(MenuItem):
    def __init__(self, name, price, is_vegetarian):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian

class MainCourse(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

class Dessert(MenuItem):
    def __init__(self, name, price, is_sugar_free):
        super().__init__(name, price)
        self.is_sugar_free = is_sugar_free

class Pepsi(Drink):
    def __init__(self, name, price, size):
        super().__init__(name, price, size)
        self.size = size

class OrangeJuice(Drink):
    def __init__(self, name, price, size):
        super().__init__(name, price, size)
        self.size = size

class GarlicBread(Entrance):
    def __init__(self, name, price, is_vegetarian):
        super().__init__(name, price, is_vegetarian)
        self.is_vegetarian = is_vegetarian

class GrilledChicken(MainCourse):
    def __init__(self, name, price, calories):
        super().__init__(name, price, calories)
        self.calories = calories

class Brownie(Dessert):
    def __init__(self, name, price, is_sugar_free):
        super().__init__(name, price, is_sugar_free)
        self.is_sugar_free = is_sugar_free

class FruitSalad(Dessert):
    def __init__(self, name, price, is_sugar_free):
        super().__init__(name, price, is_sugar_free)
        self.is_sugar_free = is_sugar_free

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.calculate_price() for item in self.items)

    def apply_discount(self, discount_percentage):
        total = self.calculate_total()
        return total - (total * discount_percentage / 100)

if __name__ == "__main__":
    order = Order()
    order.add_item(Drink("Coke", 2.5, "Medium"))
    order.add_item(Entrance("Spring Rolls", 5.0, True))
    order.add_item(MainCourse("Steak", 15.0, 800))
    order.add_item(Dessert("Cheesecake", 6.0, False))
    order.add_item(Drink("Pepsi", 2.0, "Large")) 
    order.add_item(Drink("Orange Juice", 3.0, "Small"))
    order.add_item(Entrance("Garlic Bread", 4.0, False))  
    order.add_item(MainCourse("Grilled Chicken", 12.0, 600)) 
    order.add_item(Dessert("Brownie", 5.0, False)) 
    order.add_item(Dessert("Fruit Salad", 4.5, True)) 

    print("Total before discount:", order.calculate_total())
    print("Total after 10% discount:", order.apply_discount(10))