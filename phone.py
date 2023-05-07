from item import Item
# Inheritance from item class

class Phone(Item):
  def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
    # called super class to use parent class attribute
    super().__init__(
      name, price, quantity
    )
    # run validations to the received arguments
    assert broken_phones >= 0, f"Broken Phone {broken_phones} is not greater than 0"

    # Assign to to self object
    self.broken_phones = broken_phones
