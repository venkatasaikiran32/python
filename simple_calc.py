""" 
it is a module basically caluclator.py because it has methods add,subtract,multiply,divide
"""



def add(a, b):
    """
    it returns the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    it returns the difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    it returns the product of a and b.
    """
    return a * b

def divide(a, b):
    """
    it returns the quotient of a and b. 
    """
    try:
        c=a/b
        return c
    except ZeroDivisionError as e:
        print("sorry you have entered denominator as 0")
        print(e)

   