"""In this module we test functionalities of the reading_data module."""
from unittest import TestCase
from reading_data import reading_csv, reading_json


class TestReadingCSV(TestCase):
    """Test for csv reader"""
    def test_reading_csv(self):
        """Check behavior of reading_csv."""
        data = reading_csv("test_data.csv")
        self.assertEqual(tuple(data[0]), (1, 2))
        self.assertEqual(tuple(data[1]), (3, 4))


class TestReadingJson(TestCase):
    """Test for json reader"""
    def test_reading_json(self):
        """Check behavior of reading_json."""
        data = reading_json("test_data.json")
        self.assertTrue(data["dog"])
        self.assertTrue(data["cat"])
