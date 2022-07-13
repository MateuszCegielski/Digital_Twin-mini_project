"""Shaft class and methods"""
import math


class Shaft:
    """The class was designed to store information about shafts.

Parameters
------------
nominal_stress : float
    A parameter of a shaft needed to calculate its safety factor
item_id  :  str
    Designation of the bearing
safety_factor : list
    If factor is lower than 1, it means that shaft is not safe.
result : float
    Results of the shaft analysis.
    Consist statistics minimum value of safety factor.
torque : float
    A parameter read from csv file, it is a torque measured by the sensor on the shaft,
    needed to calculate real_stress and safety_factor
"""
    def __init__(self, nominal_stress, id_shaft, diameter):
        self.nominal_stress = nominal_stress
        self.item_id = id_shaft
        self.diameter = diameter
        self.safety_factor = []
        self.result = None

    def calculate_safety_factor(self, torque):
        """Calculating the durability of shafts"""
        real_stress = (torque * 32) / (math.pi * self.diameter ** 3)
        self.safety_factor.append(self.nominal_stress / real_stress)

    def create_final_data(self):
        """Calculating minimum safety factor """
        min_value = min(self.safety_factor)
        self.result = round(min_value, 2)
