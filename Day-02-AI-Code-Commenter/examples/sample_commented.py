# Calculates the area of a rectangle given its length and width.
def calculate_area(length, width):
    return length * width


# Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


class Cart:
    # Initializes an empty list to store items for the object instance.
    def __init__(self):
        self.items = []

    # Calculates the total cost by summing the product of price and quantity for each item.
    def total(self):
        return sum(price * qty for price, qty in self.items)
