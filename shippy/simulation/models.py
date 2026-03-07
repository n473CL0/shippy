"""
Author: Viktor
Description: Core data models and constants
"""

from dataclasses import dataclass
from data_extraction import VLSFO_Price, EU_ETS_Price

# 1. Vessels

@dataclass(frozen=True)
class Vessel:
    """
    Immutable class for vessel.
    """
    name: str
    lenght: float
    operating_days: int
    share_in_EU_ETS: float
    fuel_consumption: float

# Dictionary of Vessels
VESSELS = {
    'Vessel A': Vessel(
        name='Vessel A',
        lenght=225,
        operating_days=345,
        share_in_EU_ETS=0.5,
        fuel_consumption=42
    )
}

# 2. Market Variables

VLSFO_Price = VLSFO_Price
EU_ETS_Price = EU_ETS_Price

print(VLSFO_Price, EU_ETS_Price)
print(VESSELS)
