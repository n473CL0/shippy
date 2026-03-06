from .models import *
from .utils import *

def yearly_increase_to_daily_rate(biofouling: biofouling):
    """Converts the yearly increase in fuel consumption due to biofouling to a daily rate."""
    return biofouling.year_increase / 365

def cleaning_period(cleaning_profile: cleaning_profile):
    """Calculates the period between cleanings in days."""
    return 365 / cleaning_profile.clean_frequency

def period_fuel_usage(cleaning_profile: cleaning_profile, biofouling: biofouling):
    """Calculates the fuel usage of the vessel over the cleaning period, taking into account the increase in fuel consumption due to biofouling."""
    daily_rate = yearly_increase_to_daily_rate(biofouling)
    period = cleaning_period(cleaning_profile)
    return cleaning_profile.post_clean_fuel_usage + 0.5 * daily_rate * period

def fuel_used(
        operating_profile: operating_profile, 
        biofouling: biofouling, 
        cleaning_profile: cleaning_profile
    ):
    """Calculates the total fuel used over the operating period, taking into account the increase in fuel consumption due to biofouling and the cleaning profile."""
    return operating_profile.operating_days * operating_profile.daily_fuel_consumption * period_fuel_usage(cleaning_profile, biofouling)

def fuel_cost(
        operating_profile: operating_profile,
        biofouling: biofouling,
        cleaning_profile: cleaning_profile
    ):
    """Calculates the total fuel cost over the operating period, taking into account the increase in fuel consumption due to biofouling and the cleaning profile."""
    return fuel_used(operating_profile, biofouling, cleaning_profile) * operating_profile.fuel_type.price

def carbon_emitted(
        operating_profile: operating_profile,
        biofouling: biofouling,
        cleaning_profile: cleaning_profile
    ):
    """Calculates the total carbon emitted over the operating period, taking into account the increase in fuel consumption due to biofouling and the cleaning profile."""
    return fuel_used(operating_profile, biofouling, cleaning_profile) * operating_profile.fuel_type.carbon_emitted

def carbon_cost(
        operating_profile: operating_profile, 
        biofouling: biofouling, 
        cleaning_profile: cleaning_profile
    ):
    """Calculates the total carbon cost over the operating period, taking into account the increase in fuel consumption due to biofouling and the cleaning profile."""
    return carbon_emitted(operating_profile, biofouling, cleaning_profile) * operating_profile.share_in_EU_ETS * operating_profile.EU_ETS_price

def service_cost(
        vessel: vessel,
        cleaning_profile: cleaning_profile
    ):
    """Calculates the total service cost over the operating period, taking into account the vessel length and the cleaning profile."""
    return vessel.length * cleaning_profile.service_price * cleaning_profile.clean_frequency

def total_cost(
        operating_profile: operating_profile,
        biofouling: biofouling,
        cleaning_profile: cleaning_profile,
        vessel: vessel
    ):
    """Calculates the total cost over the operating period, taking into account the fuel cost, carbon cost, and service cost."""
    return fuel_cost(operating_profile, biofouling, cleaning_profile) + carbon_cost(operating_profile, biofouling, cleaning_profile) + service_cost(vessel, cleaning_profile)

def year_payback(
        operating_profile: operating_profile,
        biofouling: biofouling,
        cleaning_profile_1: cleaning_profile,
        cleaning_profile_2: cleaning_profile,
        vessel: vessel,
        detailed: bool=False
    ):
    """Calculates the payback period in years for switching from cleaning_profile_1 to cleaning_profile_2, taking into account the fuel cost, carbon cost, and service cost."""

    fuel_difference = fuel_cost(operating_profile, biofouling, cleaning_profile_2) - fuel_cost(operating_profile, biofouling, cleaning_profile_1)
    carbon_difference = carbon_cost(operating_profile, biofouling, cleaning_profile_2) - carbon_cost(operating_profile, biofouling, cleaning_profile_1)
    service_difference = service_cost(vessel, cleaning_profile_2) - service_cost(vessel, cleaning_profile_1)
    total_difference = fuel_difference + carbon_difference + service_difference

    if detailed:
        return fuel_difference, carbon_difference, service_difference, total_difference

    return total_difference