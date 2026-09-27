def calculate_area(length, width):
    return length * width


def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


class Cart:
    def __init__(self):
        self.items = []

    def total(self):
        return sum(price * qty for price, qty in self.items)