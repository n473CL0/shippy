class CleaningProfile():
    
    def __init__(
        self,
        post_clean_efficiency: float,
        clean_frequency: int,
        service_price: float
    ):
        self.post_clean_efficiency = post_clean_efficiency
        self.clean_frequency = clean_frequency
        self.cleaning_period = 365 / clean_frequency
        self.service_price = service_price