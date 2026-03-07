from data_extraction import VLSFO_Price
class FuelType():

    def __init__(
        self,
        price: float,
        carbon_emitted: float
    ):
        self.price = price
        self.co2_emmissions = carbon_emitted

VLSFO = FuelType(
    price=VLSFO_Price,
    carbon_emitted=3.151
)