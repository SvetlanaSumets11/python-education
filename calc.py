"""This module contains simple calculator implementation"""


class Calculator:
    """This class for simple binary operations between real numbers"""
    @staticmethod
    def add(first, second):
        """Function for adding two numbers

        Parameters:
        first (float): A decimal integer
        second (float): Another decimal integer

        Returns:
        int or float: The result of adding two numbers"""
        return first + second

    @staticmethod
    def sub(first, second):
        """Function for substraction two numbers

        Parameters:
        first (float): A decimal integer
        second (float): Another decimal integer

        Returns:
        int or float: The result of substraction two numbers"""
        return first - second

    @staticmethod
    def mul(first, second):
        """Function for multiplying two numbers

        Parameters:
        first (float): A decimal integer
        second (float): Another decimal integer

        Returns:
        int or float:The result of multiplying two numbers"""
        return first * second

    @staticmethod
    def div(first, second):
        """Function for dividing two numbers

        Parameters:
        first (float): A decimal integer
        second (float): Another decimal integer

        Returns:
        int or float: The result of dividing two numbers"""
        return first / second


print(Calculator.add(2, 2))
print(Calculator.sub(2, 2))
print(Calculator.mul(2, 2))
print(Calculator.div(2, 2))
