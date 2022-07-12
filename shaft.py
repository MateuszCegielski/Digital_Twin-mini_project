""""The model of shaft with required parameters to calculate it"""
import math


class Shaft:
    """The class of bearing with constructor and two methods"""
    def __init__(self, nominal_stress, id_shaft, diameter):
        self.ns_attribute = nominal_stress
        self.item_id = id_shaft
        self.diameter = diameter
        self.si_attribute = []
        self.result = []

    def calculate_durability(self, torque):
        """Calculating the durability of shafts"""
        real_stress = (torque * 32) / (math.pi * self.diameter)
        self.si_attribute.append(self.ns_attribute/real_stress)

    def create_final_data(self):
        """Calculating minimum"""
        min_value = min(self.si_attribute)
        self.result = min_value
