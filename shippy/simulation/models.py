"""
Author: Viktor
Description: Core data models and constants
"""

from dataclasses import dataclass
from data_extraction import VLSFO_Price, EU_ETS_Price, USD_GBP

# 1. Vessels

@dataclass(frozen=True)
class Vessel:
    """
    Immutable class for vessel.
    """
    name: str
    length: float
    operating_days: int
    share_in_EU_ETS: float
    fuel_consumption: float

# Dictionary of Vessels
VESSELS = {
    'Vessel A': Vessel(
        name='Vessel A',
        length=355,
        operating_days=340,
        share_in_EU_ETS=0.5,
        fuel_consumption=163
    ),
    'Vessel B': Vessel(
        name='Vessel B',
        length=245,
        operating_days=315,
        share_in_EU_ETS=0.65,
        fuel_consumption=45
    ),
    'Vessel C': Vessel(
        name='Vessel C',
        length=290,
        operating_days=315,
        share_in_EU_ETS=0.2,
        fuel_consumption=43
    )
}

# 2. Market Variables

VLSFO_Price = VLSFO_Price
EU_ETS_Price = EU_ETS_Price


# 3. CleaningProfile Variables

@dataclass(frozen=True)
class CleaningProfile:
    """
    Immutable hull cleaning service profiles.
    """
    name: str
    post_clean_efficiency: float
    clean_frequency: int
    service_price: float

# Dictionary of Services (ScrubMarine and Alternative)
SERVICES = {
    'ScrubMarine': CleaningProfile(
        name='Scrub Marine',
        post_clean_efficiency=1.05,
        clean_frequency=4,
        service_price=300*USD_GBP,
    ),
    'Alternative': CleaningProfile(
        name='Alternative',
        post_clean_efficiency=1.10,
        clean_frequency=3,
        service_price=500*USD_GBP,
    )
}