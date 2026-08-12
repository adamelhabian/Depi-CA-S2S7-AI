'''
 This file responsible for make the logic of calulator 
 perform addition , subtraction , multiplication and divition
'''

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2