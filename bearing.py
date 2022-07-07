""""The model of bearing with required parameters to calculate it"""

from statistics import mean


class Bearing:
    """The class of bearing with constructor and two methods"""
    def __init__(self, dynamic_load_capacity, id_bearing):
        self.c_attribute = dynamic_load_capacity
        self.item_id = id_bearing
        self.l_attribute = []
        self.result = []

    def calculate(self, force):
        """Calculating the durability of bearings"""
        self.l_attribute.append(self.c_attribute / force)

    def creating_final_data(self):
        """Calculating statistics such as mean, minimum, maximum in one list"""
        min_value = min(self.l_attribute)
        mean_value = mean(self.l_attribute)
        max_value = max(self.l_attribute)
        self.result = [min_value, mean_value, max_value]
