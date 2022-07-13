"""Bearing class and methods"""
from statistics import mean

class Bearing:
    """The class was designed to store information about bearings.

Parameters
------------
dynamic_load_capacity : float
    A parameter of a bearing needed to calculate its expected life
item_id  :  str
    Designation of the bearing
nominal_fatigue_life : list
    Unit of nominal  fatigue life : millions of rotations
result : dict
    Results of the bearing analysis.
    Consist statistics such as mean, minimum, maximum in one dictionary
force : float
    A parameter read from csv file, it is a force measured by the sensor on the bearing,
     needed to calculate expected life
"""

    def __init__(self, dynamic_load_capacity, id_bearing):
        self.dynamic_load_capacity = dynamic_load_capacity
        self.item_id = id_bearing
        self.nominal_fatigue_life = []
        self.result = []

    def calculate_durability(self, force):
        """Calculating the durability of bearings.
         Unit of nominal  fatigue life : millions of rotations"""
        self.nominal_fatigue_life.append((self.dynamic_load_capacity / force) ** 3)

    def create_final_data(self):
        """Calculating statistics such as mean, minimum, maximum in one dict"""
        min_value = min(self.nominal_fatigue_life)
        mean_value = mean(self.nominal_fatigue_life)
        max_value = max(self.nominal_fatigue_life)
        self.result = {"min_durability": round(min_value, 2),
                       "mean_durability": round(mean_value, 2),
                       "max_durability": round(max_value, 2)
                       }
