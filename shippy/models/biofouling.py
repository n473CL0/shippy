from .cleaning_profile import CleaningProfile

class Biofouling():

    def __init__(
        self,
        year_increase: float,
     ):
        self.year_increase = year_increase
        self.daily_rate = year_increase / 365

    def period_efficiency(self, cleaningProfile: CleaningProfile):
        return cleaningProfile.post_clean_efficiency + 0.5 * self.daily_rate * cleaningProfile.cleaning_period