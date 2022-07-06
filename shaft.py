class Shaft:
    def __init__(self, nominal_stress, allowed_stress, safety_indicator, id, allowed_safety_indicator = None):
        self.As = allowed_stress
        self.Ns = nominal_stress
        self.Si = safety_indicator
        self.name = id
        self.allowed_safety_indicator = allowed_safety_indicator

    # def print_parameters(self):
    #     print(f"The shaft named {self.name}. Parameters: {self.Ns} nominal_stress, {self.As} allowed_stress.")
    def __calculate__(self):
        self.Si = self.Ns / self.As
        return float(self.Si)

    def print_result(self):
        print(f" The saftey indicator of shaft is equal to {self.Si}.\n")
        if {self.Si} < {self.safety_indicator}:
            print(f"{self.Si} is optimal, the {self.name} shaft is able to work.\n")
        else:
            print(f"{self.Si} is too high, the {self.name} shaft is broken.\n")


class ListOfShafts(Shaft):
    def __int__(self, bearing_list):
        self.bearing_list = bearing_list