"""
A module of mathematical classes and functions that were made without importing any\n
libraries. This is being actively worked on as an exercise in coding.\n
Note: some of it is stuff nobody would ever need ever I just wanted to do it.
"""

myPi = 3.141592653589793
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
    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
    def __str__(self):
        return f"({self.x}, {self.y})"

class Circle:
    """Handles all the math (that I can think of) that you might need for a circle."""
    def __init__(self, radius = 2.0):
        self.radius = radius

    @property
    def area(self):
        """Calculate the area of a circle with a given radius."""
        return float(f"{myPi * self.radius ** 2:.4f}") #-- if anybody has a cleaner way to achieve this please let me know
    
    @property
    def circumference(self):
        """Calculate the circumference of a circle with a given radius."""
        return float(f"{2 * myPi * self.radius:.4f}") #-- if anybody has a cleaner way to achieve this please let me know

    @property
    def diameter(self):
        """Returns the diameter of a circle with a given radius."""
        return self.radius * 2

    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __str__(self):
        return f"A circle of radius of {self.radius} units."

class NumericalStatistics:
    """A class to handle all the statistics I can remember."""
    def __init__(self, numbers = []):
        self.numbers = numbers

    @property
    def mean(self):
        """Returns the average for a given list of numbers."""
        sum = 0
        for number in self.numbers:
            sum += number
        return sum / len(self.numbers)
    
    @property
    def median(self):
        """Returns the middle value for a given list of numbers."""
        self.numbers.sort()
        if len(self.numbers) % 2 == 1:
            index = (len(self.numbers) // 2)
            return self.numbers[index]
        else:
            indexA, indexB = int((len(self.numbers) / 2)), int((len(self.numbers) / 2) - 1)
            return (self.numbers[indexA] + self.numbers[indexB]) / 2
        
    @property
    def mode(self):
        """Returns the most common number among a list of numbers."""
        numberTracker = {f"{number}" : 0 for number in set(self.numbers)}
        for numberElement in self.numbers:
            numberTracker[f"{numberElement}"] += 1
        mostOccurances = max(set(numberTracker.values()))
        mostCommonNumber = [int(numberKey) for numberKey, numberValue in numberTracker.items() if numberValue == mostOccurances]
        return mostCommonNumber
    
    @property
    def uniqueItems(self):
        """Returns a set of unique items in the list of numbers."""
        return set(self.numbers)
    
    def __repr__(self):
        return f"NumericalStatistics({self.numbers})"
    
    def __str__(self):
        return f"A list of numbers that includes the set {set(self.numbers)}."

class Rectangle:
    """Handles all the math (that I can think of) that you might need for a rectangle."""
    def __init__(self, length = 1, width = 1):
        self.length = length
        self.width = width

    @property
    def area(self):
        """Returns the area of a rectangle of given length and width."""
        return self.length * self.width
    
    @property
    def diagonal(self):
        """Returns the diagonal measurement of a rectangle of given length and width."""
        return square_root(((self.length ** 2) + (self.width ** 2)))
    
    @property
    def is_square(self):
        """Is this rectangle a square?"""
        return self.length == self.width

    @property
    def perimeter(self):
        """Returns the length of the perimeter of a rectangle of given length and width."""
        return (self.length * 2) + (self.width * 2)
    
    def __repr__(self):
        return f"Rectangle({self.length, self.width})"
    
    def __str__(self):
        return f"A rectangle of length {self.length} units and width {self.width} units."

class Triangle:
    """Handles all the math (that I can think of) that you might need for a triangle."""
    def __init__(self, sideOne = 1.0, sideTwo = 1.0, sideThree = 1.0):
        self.sideOne = sideOne
        self.sideTwo = sideTwo
        self.sideThree = sideThree
        self.perimeter = sideOne + sideTwo + sideThree
        self.semiperimeter = self.perimeter / 2

    @property
    def area(self):
        """Returns the area of a triangle of given base length and height length."""
        return float(f"{square_root(self.semiperimeter * (self.semiperimeter - self.sideOne) * (self.semiperimeter - self.sideTwo) * (self.semiperimeter - self.sideThree)):.4f}") #-- if anybody has a cleaner way to achieve this please let me know
    
    def __repr__(self):
        return f"Triangle({self.sideOne}, {self.sideTwo}, {self.sideThree})"
    
    def __str__(self):
        return f"A triangle with side lengths of {self.sideOne}, {self.sideTwo}, {self.sideThree}."

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
    pass
