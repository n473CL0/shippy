from .vessel import Vessel
class Fleet():

    def __init__(
            self,
            vessels: dict[Vessel, int] # vessel instance -> n of vessels in fleet
    ):
        self.vessels = vessels

    def calculate_fuel_used(self):
        return sum(vessel.calculate_fuel_used() * count for vessel, count in self.vessels.items())

    def calcualte_fuel_cost(self):
        return sum(vessel.calculate_fuel_cost() * count for vessel, count in self.vessels.items())
    
    def calculate_carbon_cost(self):
        return sum(vessel.calculate_carbon_cost() * count for vessel, count in self.vessels.items())
    
    def calculate_service_cost(self):
        return sum(vessel.calculate_service_cost() * count for vessel, count in self.vessels.items())
    
    def calculate_total_cost(self):
        return sum(vessel.calculate_total_cost() * count for vessel, count in self.vessels.items())