"""In this module we test functionalities of the bearing module."""
from statistics import mean
from unittest import TestCase
from bearing import Bearing


class TestShaft(TestCase):
    """Test for bearin."""
    def test_calculate(self):
        """Check behavior of calculate."""
        bearing1 = Bearing(5, "b232")
        l_attribute = [0.5]
        bearing1.calculate(10)
        self.assertEqual(l_attribute, bearing1.l_attribute)

    def test_creating_final_data(self):
        """Check behavior of creating final data."""
        bearing1 = Bearing(5, "b232")
        bearing1.l_attribute = [123, 700, 23, 23, 32, 1]
        bearing1.creating_final_data()
        minimum = min(bearing1.l_attribute)
        maximum = max(bearing1.l_attribute)
        mean1 = mean(bearing1.l_attribute)
        self.assertEqual([minimum, mean1, maximum], bearing1.result)
