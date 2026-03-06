from collections import namedtuple as namedtuple

biofouling = namedtuple("biofouling", ["year_increase"])

cleaning_profile = namedtuple("cleaning_profile", ["post_clean_fuel_usage", "clean_frequency", "service_price"])

fuel_type = namedtuple("fuel_type", ["price", "carbon_emitted"])

# Just including one fuel type per profile for now, but this can be easily to include more fuel types.
operating_profile = namedtuple("operating_profile", ["operating_days", "share_in_EU_ETS", "EU_ETS_price", "fuel_type", "daily_fuel_consumption"])

vessel = namedtuple("vessel", ["length"])