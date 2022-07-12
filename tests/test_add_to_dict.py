"""In this module we test functionalities of the add to dict module."""

from unittest import TestCase
from utilities import add_to_dict


class TestAddToDict(TestCase):
    """Test for add to dict."""
    def test_adding_to_dict(self):
        """Check behavior of adding to dict."""
        original_dict = {
            "name": ["Tom", "Jerry", "Konrad"],
            "surname": ["Kowalski", "Szpak", "Bielik"]
        }
        test_dict = {}
        add_to_dict(test_dict, "name", "Tom")
        add_to_dict(test_dict, "name", "Jerry")
        add_to_dict(test_dict, "name", "Konrad")
        add_to_dict(test_dict, "surname", "Kowalski")
        add_to_dict(test_dict, "surname", "Szpak")
        add_to_dict(test_dict, "surname", "Bielik")
        self.assertEqual(test_dict, original_dict)
