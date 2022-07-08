"""In this module we test functionalities of the add to dict module."""

from unittest import TestCase
from add_to_dict import adding_to_dict


class TestAddToDict(TestCase):
    """Test for add to dict."""
    def test_adding_to_dict(self):
        """Check behavior of adding to dict."""
        original_dict = {
            "name": ["Tom", "Jerry", "Konrad"],
            "surname": ["Kowalski", "Szpak", "Bielik"]
        }
        test_dict = {}
        adding_to_dict(test_dict, "name", "Tom")
        adding_to_dict(test_dict, "name", "Jerry")
        adding_to_dict(test_dict, "name", "Konrad")
        adding_to_dict(test_dict, "surname", "Kowalski")
        adding_to_dict(test_dict, "surname", "Szpak")
        adding_to_dict(test_dict, "surname", "Bielik")
        self.assertEqual(test_dict, original_dict)
