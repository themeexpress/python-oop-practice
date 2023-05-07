import csv

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

  @classmethod
  def instantiate_from_csv(cls):
    with open('items.csv', 'r') as f:
      reader = csv.DictReader(f)
      items = list(reader)

    for item in items:
      print(item)

  def __repr__(self) -> str:
    return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
