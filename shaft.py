""""The model of shaft with required parameters to calculate it"""
import math


class Shaft:
    """The class of bearing with constructor and two methods"""
    def __init__(self, nominal_stress, id_shaft, diameter):
        self.nominal_stress = nominal_stress
        self.item_id = id_shaft
        self.diameter = diameter
        self.safety_factor = []
        self.result = []

    def calculate_durability(self, torque):
        """Calculating the durability of shafts"""
        real_stress = (torque * 32) / (math.pi * self.diameter ** 3)
        self.safety_factor.append(self.nominal_stress / real_stress)

    def create_final_data(self):
        """Calculating minimum safety factor """
        min_value = min(self.safety_factor)
        self.result = min_value
