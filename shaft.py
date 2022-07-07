import math
from statistics import mean


class Shaft:

    def __init__(self, nominal_stress, id, diameter):
        self.Ns = nominal_stress
        self.id = id
        self.diameter = diameter
        self.Si = []
        self.result = []

    def calculate(self, torque):
        real_stress = (torque * 32) / (math.pi * self.diameter)
        self.Si.append(self.Ns/real_stress)

    def print_result(self):
        print(f" The saftey indicator of shaft is equal to {self.Si}.\n")
        if {self.Si} < {self.safety_indicator}:
            print(f"{self.Si} is optimal, the {self.id} shaft is able to work.\n")
        else:
            print(f"{self.Si} is too high, the {self.id} shaft is broken.\n")

    def creating_final_data(self):
        min_value = min(self.Si)
        self.result = min_value
