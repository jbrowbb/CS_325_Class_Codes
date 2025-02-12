import pytest

from area import calculate_area

def test_positive_area():
  """Tests area calculation with positive values."""
  assert calculate_area(5, 3) == 15


def test_zero_area():
  """Tests area calculation with zero values."""
  assert calculate_area(0, 10) == 0
  assert calculate_area(5, 0) == 0


def test_negative_values():
  """Tests handling of negative values."""
  with pytest.raises(ValueError):
    calculate_area(-2, 4)
  with pytest.raises(ValueError):
    calculate_area(3, -1)