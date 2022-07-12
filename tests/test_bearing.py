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
        bearing1.calculate_durability(10)
        self.assertEqual(l_attribute, bearing1.nominal_fatigue_life)

    def test_creating_final_data(self):
        """Check behavior of creating final data."""
        bearing1 = Bearing(5, "b232")
        bearing1.nominal_fatigue_life = [123, 700, 23, 23, 32, 1]
        bearing1.creating_final_data()
        minimum = min(bearing1.nominal_fatigue_life)
        maximum = max(bearing1.nominal_fatigue_life)
        mean1 = mean(bearing1.nominal_fatigue_life)
        self.assertEqual([minimum, mean1, maximum], bearing1.result)
