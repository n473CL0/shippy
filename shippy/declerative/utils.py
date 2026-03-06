def net_present_value(
        yearly_savings: float,
        discount_rate: float,
        years: int
    ):
    """Calculates the net present value of a series of yearly savings, given a discount rate and number of years."""
    npv = 0
    for year in range(1, years + 1):
        npv += yearly_savings / (1 + discount_rate) ** year
    return npv