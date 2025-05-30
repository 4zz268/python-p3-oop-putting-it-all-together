import pytest
from lib.shoe import Shoe

def test_shoe_initialization():
    shoe = Shoe("Nike", 10)
    assert shoe.brand == "Nike"
    assert shoe.size == 10
    assert shoe.condition == "New"

def test_shoe_size_validation():
    shoe = Shoe("Adidas", 9)
    shoe.size = "large"
    assert shoe.size == 9  # Should not change to invalid value
    shoe.size = 11
    assert shoe.size == 11

def test_shoe_cobble():
    shoe = Shoe("Puma", 8)
    shoe.condition = "Used"
    shoe.cobble()
    assert shoe.condition == "New"
