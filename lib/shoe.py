# Shoe class for OOP lab
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self._condition = "New"

    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, (int, float)):
            self._size = value
        else:
            print("size must be a number")

    size = property(get_size, set_size)

    def get_condition(self):
        return self._condition

    def set_condition(self, value):
        self._condition = value

    condition = property(get_condition, set_condition)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
