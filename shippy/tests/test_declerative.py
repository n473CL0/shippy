import shippy.declerative as shipdec
import math

def test_init():

    clean = shipdec.cleaning_profile(post_clean_fuel_usage=1.05, clean_frequency=4, service_price=220)
    assert clean is not None
    assert math.isclose(shipdec.cleaning_period(clean), 91.25)

    bio = shipdec.biofouling(year_increase=0.3)
    assert bio is not None
    assert math.isclose(shipdec.yearly_increase_to_daily_rate(bio), 0.3 / 365)
    assert math.isclose(shipdec.period_fuel_usage(clean, bio), 1.0875)

    vlsfo = shipdec.fuel_type(price=380, carbon_emitted=3.1)
    assert vlsfo is not None

    opp = shipdec.operating_profile(
        operating_days=345,
        share_in_EU_ETS=0.5,
        EU_ETS_price=62.51,
        fuel_type=vlsfo,
        daily_fuel_consumption=163.0
    )
    assert opp is not None
    assert math.isclose(shipdec.fuel_used(opp, bio, clean), 345 * 163.0 * 1.0875)
    assert math.isclose(shipdec.fuel_cost(opp, bio, clean), 345 * 163.0 * 1.0875 * 380)
    assert math.isclose(shipdec.carbon_emitted(opp, bio, clean), 345 * 163.0 * 1.0875 * 3.1)
    assert math.isclose(shipdec.carbon_cost(opp, bio, clean), 345 * 163.0 * 1.0875 * 3.1 * 0.5 * 62.51)

    v = shipdec.vessel(length=370)
    assert v is not None
    assert math.isclose(shipdec.service_cost(v, clean), 370 * 220 * 4)
    assert math.isclose(shipdec.total_cost(opp, bio, clean, v), 29490106.78)

    clean_alt = shipdec.cleaning_profile(post_clean_fuel_usage=1.1, clean_frequency=3, service_price=300)

    fuel_difference, carbon_difference, service_difference, total_difference = shipdec.year_payback(opp, bio, clean, clean_alt, v, detailed=True)
    assert math.isclose(fuel_difference, 1335581.25)
    assert math.isclose(carbon_difference, 340539.83, rel_tol=0.1)
    assert math.isclose(service_difference, 7400.00)
    assert math.isclose(total_difference, 1683521.08)

    assert math.isclose(shipdec.net_present_value(yearly_savings=total_difference, discount_rate=0.08, years=10),  11296563.48)