from shippy.models import CleaningProfile, Biofouling, OperatingProfile, FuelType, Vessel
import math

# Some testing functions to check the code is producing the same numbers as the excel model.

def test_cleaning_profile():
    
    cleaning_profile = CleaningProfile(1.05, 4, 220)

    assert cleaning_profile is not None
    assert cleaning_profile.cleaning_period == 91.25


def test_linear_biofouling():

    cleaning_profile = CleaningProfile(1.05, 4, 220)
    biofouling = Biofouling(0.3)

    assert biofouling is not None
    assert math.isclose(biofouling.period_efficiency(cleaning_profile), 1.0875)

def test_operating_profile():

    vlsfo = FuelType(price=380, carbon_emitted=3.1)
    fuel_types = { vlsfo : 163.0 }

    operating_profile = OperatingProfile(
        operating_days=345, 
        share_in_EU_ETS=0.5, 
        EU_ETS_price=62.51, 
        fuel_types=fuel_types
    )

    assert operating_profile is not None
    assert operating_profile.baseline_fuel_cost() == 163 * 345 * 380
    assert operating_profile.baseline_carbon_emitted() == 163 * 345 * 3.1

def test_vessel():

    cleaning_profile = CleaningProfile(post_clean_efficiency=1.05, clean_frequency=4, service_price=220)
    biofouling = Biofouling(year_increase=0.3)

    vlsfo = FuelType(price=380, carbon_emitted=3.1)
    fuel_types = { vlsfo : 163.0 }
    
    operating_profile = OperatingProfile(
        operating_days=345, 
        share_in_EU_ETS=0.5, 
        EU_ETS_price=62.51, 
        fuel_types=fuel_types
    )

    vessel = Vessel(
        length=370,
        operating_profile=operating_profile,
        biofouling_model=biofouling,
        cleaning_profile=cleaning_profile
    )

    assert vessel is not None
    assert math.isclose(vessel.calculate_fuel_used(), 61155.5625)
    assert math.isclose(vessel.calculate_fuel_cost(), 23239113.75)
    assert math.isclose(vessel.calculate_carbon_cost(), 5925393.03)
    assert math.isclose(vessel.calculate_service_cost(), 325600.00)
