class Item:
  pay_rate = 0.8 # The pay rate after 20% discount
  all = []
  def __init__(self, name: str, price: float, quantity: int):
    # run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than 0"
    assert quantity >= 0, f"Quantity {quantity} is not greater than 0"
    # Assign to to self object
    self.name = name
    self.price = price
    self.quantity = quantity

    # actions ti execution
    Item.all.append(self)
  

  def calculate_total_price(self):
    return self.price * self.quantity

  def apply_discount(self):
    self.price = self.price * self.pay_rate


# Create an object from class
# item1 = Item('iPhone', 100, 1)
# item1.apply_discount()
# print(item1.price)

# item2 = Item('Mac', 1000, 3)
# item2.price = 0.7
# item2.apply_discount()
# print(item2.price)

item1 = Item('iPhone', 1000, 1)
item2 = Item('laptop', 10000, 4)
item3 = Item('camera', 500, 6)
item4 = Item('iwatch', 300, 8)
item5 = Item('pendrive', 100, 11)

print(Item.all)

for item in Item.all:
  print(item.name)
