from typing import (
    Annotated,
    List,
)  # Annotated is used to add context. List is used to -- suport lists -- haha self explanatory
from arcade.sdk import tool  # Decorator to integrate it with arcade AI flow
import math  # For mathematical operations


@tool
def add(
    a: Annotated[int, "The first number"], b: Annotated[int, "The second number"]
) -> Annotated[int, "The sum of the two numbers"]:
    """
    Add two numbers together
    """
    return a + b


@tool
def subtract(
    a: Annotated[int, "The first number"], b: Annotated[int, "The second number"]
) -> Annotated[int, "The difference of the two numbers"]:
    """
    Subtract two numbers
    """
    return a - b


@tool
def multiply(
    a: Annotated[int, "The first number"], b: Annotated[int, "The second number"]
) -> Annotated[int, "The product of the two numbers"]:
    """
    Multiply two numbers together
    """
    return a * b


@tool
def divide(
    a: Annotated[int, "The numerator"], b: Annotated[int, "The denominator"]
) -> Annotated[float, "The quotient of the two numbers"]:
    """
    Divide two numbers
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b


@tool
def sqrt(
    x: Annotated[float, "The number to find the square root of"]
) -> Annotated[float, "The square root of the number"]:
    """
    Calculate the square root of a number
    """
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)


@tool
def sum_list(
    numbers: Annotated[List[int], "A list of numbers to sum"]
) -> Annotated[int, "The sum of the list of numbers"]:
    """
    Sum all numbers in a list
    """
    return sum(numbers)


@tool
def sum_range(
    start: Annotated[int, "The starting integer"], end: Annotated[int, "The ending integer (exclusive)"]
) -> Annotated[int, "The sum of integers from start to end-1"]:
    """
    Sum all integers in a specified range
    """
    if start > end:
        raise ValueError("Start must be less than or equal to end.")
    return sum(range(start, end))
