square_root = lambda x: x ** 0.5

class Vector2:
    """An attempt to recreate the Vector2 class from Godot in Python for more or less educational purposes."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x * other.x, self.y * other.y)
    def __floordiv__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x // other.x, self.y // other.y)
    def __truediv__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x / other.x, self.y / other.y)
    def __pow__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x ** other.x, self.y ** other.y)
    def __mod__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x % other.x, self.y % other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

def average_die_throw(numberOfSides = 6, numberOfDice = 1):
    """Returns the average of a given number of dice of a given size."""
    averageForOneDie = (numberOfSides + 1) / 2
    return averageForOneDie * numberOfDice

def binary_addition(*numbers):
    """Adds decimal numbers and returns the sum in binary."""
    total = 0
    for number in numbers:
        total += number
    return bin(total)

def factorial(n):
    """Multiplies all integers from 1 to n (i.e. 1 * 2 * 3 * ... * n-2 * n-1 * n)"""
    if n == 0:
        n = 1
    for i in range(1, n):
        n = n * i
    return n

def golden_ratio():
    """Returns an approximation of the golden ratio."""
    return ((1 + square_root(5)) / 2)

def hexadecimal_addition(*numbers):
    """Adds decimal numbers and returns the sum in hexidecimal."""
    total = 0
    for number in numbers:
        total += number
    return hex(total)

def number_of_digits_in_the_product_of_n_to_the_power_of_n(n):
    """Returns the length of the product of n to the power of itself."""
    n = n ** n
    return len(str(n))

def octal_addition(*numbers):
    """Adds decimal numbers and returns the sum in octal."""
    total = 0
    for number in numbers:
        total += number
    return oct(total)

def sum_of_integers_up_to(n):
    """Adds all integers from 1 to n (i.e. 1 + 2 + 3 + ... + n-2 + n-1 + n)"""
    for i in range(1, n):
        n += i
    return n

def x_to_the_power_of_y(x, y):
    """Returns the product of x to the power of y."""
    return x ** y

if __name__ == "__main__":
    print(sum_of_integers_up_to(10000))
