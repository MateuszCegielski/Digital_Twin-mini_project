class Bearing:

    def __init__(self, dynamic_load_capacity, id, durability= None):
        self.L= durability
        self.C = dynamic_load_capacity
        self.name = id
    # def print_parameters(self):
    #     print(f"The bearing named {self.name}. Parameters: {self.C} dynamic load capacity, {self.P} load.")
    def calculate (self):
        self.L = self.C/self.P
        return float(self.L)

    def print_result(self):
        print(f" The durability of bearing is equal to {self.L}.\n")
        if {self.L} >= {self.allowed_durability}:
            print(f"{self.L} is too high, the {self.name} bearing is broken.\n")
        else:
            print(f"{self.L} is optimal, the {self.name} bearing is able to work.\n")



class ListOfItems (Bearing):
    def __int__(self, bearing_list):
        self.bearing_list = bearing_list

if __name__ == "__main__":
    list_of_bearing = plik
    list_of_shafts = plik
    if "bearing" in list_of_bearing:
        for bearing in list_of_bearing:
            bearing.calculate()
    elif "shaft" in list_of_shafts:
        for shaft in list_of_shafts:
            shaft.calculate()