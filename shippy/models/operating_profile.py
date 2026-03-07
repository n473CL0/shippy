from .fuel_type import FuelType
from .data_extraction import EU_ETS_Price

class OperatingProfile():

    def __init__(
        self,
        operating_days: int,
        share_in_EU_ETS: float,
        fuel_types: dict[FuelType, float], # number of tonnes consumed daily
        EU_ETS_price: float = EU_ETS_Price,
    ):
        self.operating_days = operating_days
        self.share_in_EU_ETS = share_in_EU_ETS
        self.EU_ETS_price = EU_ETS_price
        self.fuel_types = fuel_types

    def baseline_fuel_used(self):
        fuel_used = 0
        for rate in self.fuel_types.values():
            fuel_used += self.operating_days * rate
        return fuel_used

    def baseline_fuel_cost(self):
        fuel_cost = 0
        for type, rate in self.fuel_types.items():
            fuel_cost += type.price * self.operating_days * rate
        return fuel_cost

    def baseline_carbon_emitted(self):
        co2_emitted = 0
        for type, rate in self.fuel_types.items():
            co2_emitted += type.co2_emmissions * self.operating_days * rate
        return co2_emitted
    
    def baseline_carbon_cost(self):
        return self.baseline_carbon_emitted() * self.EU_ETS_price * self.share_in_EU_ETS
    
