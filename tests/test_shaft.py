"""In this module we test functionalities of the shaft module."""
from unittest import TestCase
from shaft import Shaft


class TestShaft(TestCase):
    """Test for shaft."""
    def test_calculate(self):
        """Check behavior of calculate."""
        shaft1 = Shaft(5, "s232", 4)
        si_attribute = [0.19634954084936207]
        shaft1.calculate(10)
        self.assertEqual(si_attribute, shaft1.si_attribute)

    def test_creating_final_data(self):
        """Check behavior of creating final data."""
        shaft1 = Shaft(1231, "1231", 1231)
        shaft1.si_attribute = [2342, 1232, 21, 1, 3]
        shaft1.create_final_data()
        minimum = min(shaft1.si_attribute)
        self.assertEqual(minimum, shaft1.result)
