import pytest
import math


from circle_class import Circle

def test_positive_area():
  """Tests area calculation with a positive radius."""
  circle = Circle(5)
  assert circle.calculate_area() == pytest.approx(25 * math.pi)  # Use approx for floating-point comparison


def test_zero_radius():
  """Tests area calculation with a zero radius."""
  circle = Circle(0)
  assert circle.calculate_area() == 0


def test_negative_radius():
  """Tests handling of negative radius."""
  with pytest.raises(ValueError):
    Circle(-2)
