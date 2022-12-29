#!/usr/bin/python3
"""
This module defines a Square class which calculates the area and
perimeter of the square from the dimensions passed in
"""


class Square:
    """
    Initialize the class variables as a default
    to fall back to
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes and set the args as instance
        variables
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Calculates the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns a string representation of the square
        dimension """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
