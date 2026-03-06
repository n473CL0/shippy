from .biofouling import Biofouling
from .cleaning_profile import CleaningProfile
from .operating_profile import OperatingProfile


class Vessel:

    def __init__(
        self,
        length: float,
        operating_profile: OperatingProfile,
        biofouling_model: Biofouling,
        cleaning_profile: CleaningProfile,
    ):
        self.length = length
        self.operating_profile = operating_profile
        self.biofouling_model = biofouling_model
        self.cleaning_profile = cleaning_profile
    
    def calculate_fuel_used(self):
        return self.operating_profile.baseline_fuel_used() * self.biofouling_model.period_efficiency(self.cleaning_profile)

    def calculate_fuel_cost(self):
        return self.operating_profile.baseline_fuel_cost() * self.biofouling_model.period_efficiency(self.cleaning_profile)
    
    def calculate_carbon_emitted(self):
        return self.operating_profile.baseline_carbon_emitted() * self.biofouling_model.period_efficiency(self.cleaning_profile)

    def calculate_carbon_cost(self):
        return self.operating_profile.baseline_carbon_cost() * self.biofouling_model.period_efficiency(self.cleaning_profile)
    
    def calculate_service_cost(self):
        return self.length * self.cleaning_profile.service_price * self.cleaning_profile.clean_frequency
    
    def calculate_total_cost(self):
        return self.calculate_fuel_cost() + self.calculate_carbon_cost() + self.calculate_service_cost()