""""The model of bearing with required parameters to calculate it"""

from statistics import mean


class Bearing:
    """The class of bearing with constructor and two methods"""
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
        """Calculating statistics such as mean, minimum, maximum in one list"""
        min_value = min(self.nominal_fatigue_life)
        mean_value = mean(self.nominal_fatigue_life)
        max_value = max(self.nominal_fatigue_life)
        self.result = {"min_durability": min_value,
                       "mean_durability": mean_value,
                       "max_durability": max_value
        }
