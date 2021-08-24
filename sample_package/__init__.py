from typing import List


class Circle:
    """A class representing a circle."""
    __slots__ = ("radius",)

    def __init__(self, radius: int) -> None:
        #: Radius of a circle.
        self.radius = radius


class Pizza(Circle):
    """A class representing a pizza."""

    def __init__(self, ingredients: List[str]) -> None:
        #: List of ingredients.
        self.ingredients = ingredients
