import math


class Circle:
  """Represents a circle with a radius."""

  def __init__(self, radius):
    """Initializes a Circle object with a radius."""
    if radius < 0:
      raise ValueError("Radius cannot be negative")
    self.radius = radius

  def calculate_area(self):
    """Calculates the area of the circle."""
    return math.pi * self.radius**2
