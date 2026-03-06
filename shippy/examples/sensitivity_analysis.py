from shippy.declerative import *

def do_sensitivity_analysis():
    """Performs a sensitivity analysis on the total cost function by varying the cleaning frequency and service price, and calculating the payback period for each combination of parameters."""
    
    # Define the base case parameters
    bio = biofouling(year_increase=0.3)
    clean = cleaning_profile(post_clean_fuel_usage=1.05, clean_frequency=4, service_price=220)
    alt_clean = cleaning_profile(post_clean_fuel_usage=1.1, clean_frequency=3, service_price=300)
    opp = operating_profile(operating_days=345, share_in_EU_ETS=0.5, EU_ETS_price=62.51, fuel_type=fuel_type(price=380, carbon_emitted=3.1), daily_fuel_consumption=163)
    v = vessel(length=370)

    # Define the ranges for the sensitivity analysis

    # Fuel price range: 300 to 500

    for fuel_price in range(300, 501, 50):
        sopp = opp._replace(fuel_type=fuel_type(price=fuel_price, carbon_emitted=3.1))
        td = year_payback(sopp, bio, clean, alt_clean, v)
        print(f"Fuel price: {fuel_price}, Total difference: {td}")

    # Carbon price range: 50 to 100

    for carbon_price in range(50, 101, 10):
        sopp = opp._replace(EU_ETS_price=carbon_price)
        td = year_payback(sopp, bio, clean, alt_clean, v)
        print(f"Carbon price: {carbon_price}, Total difference: {td}")

do_sensitivity_analysis()
    