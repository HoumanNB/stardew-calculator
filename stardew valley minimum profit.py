class Earning:

    # variable assignment
    def __init__(self, seed_price: int, days_to_mature: int,  Profit_margin: int = 100, days: int = 28, number_of_crops: int = 1):
        # Error Rising For Wrong Value Types
        if seed_price < 0:
            raise ValueError("Seed Price must not be negative")

        if days_to_mature < 0:
            raise ValueError("Maturity days mand not be negative")

        if number_of_crops < 0:
            raise ValueError("Number of crops mand not be negative")

        # Raw Variable Assignment
        self.value = seed_price
        self.crops = number_of_crops
        self.mdays = days_to_mature - 1
        self.duration = days
        self.profit_margin = Profit_margin

        # Profit Margin Calculation
        if self.profit_margin < 0:
            raise ValueError("The profit margin must not be negative")
        self.margin = (self.profit_margin * 1 / 100) + 1

        # ---Single Crop Profit---
        if self.duration < self.mdays or self.duration < 0:
            raise ValueError("The number of growing days must be grater than maturity time of the crop and negative")
        self.sell_price = self.value * self.margin
        

        self.max_harvest = self.mdays // self.duration
        self.minimum_profit_per_crop = ((self.max_harvest * self.sell_price) - self.value)

        # ---Duration Profit---
        if self.duration < self.mdays or self.duration < 0:
            raise ValueError("The number of growing days must be grater than maturity time of the crop and not negative")
        else:
            self.sell_price = self.value * self.margin

        self.max_harvest = self.mdays // self.duration
        self.minimum_profit_in_duration = ((self.max_harvest * self.sell_price) - self.value) // self.duration

        # ---Multiple Crop Profit---
        self.multiple_profit = self.minimum_profit_in_duration * self.crops
        
        # --- Printing The Info After Initiation---
        
        print(f"""Minimum profit per crop: {self.sell_price}\n
                  Minimum profit in a duration: {self.minimum_profit_in_duration}\n
                  Multiple crop profit: {self.multiple_profit}""")
        # profit calculation on sell

    def results(self):
        print(f"""The minimum profit per crop is {self.sell_price}Gs. \n
                  The minimum profit during the span of {self.duration} days is about {self.minimum_profit_in_duration}. \n
                  The minimum profit for multiple crops({self.crops}) in a duration of {self.duration} days is about {self.multiple_profit}Gs""")

    def show_info(self):
        print(f"""
                  Seed price: {self.value}\n
                  Maturity days of the crop is: {self.mdays}\n
                  Profit margin percentage is: %{self.profit_margin}. (the crop's sell price will multiply by {self.margin}*)\n
                  The maximum harvests per month(or entered duration) is {self.max_harvest} times.\n
               """)
        
    @staticmethod
    def show_formulas():
        print("""
              single crop profit: (max harvest * sell price) - seed price\n
              profit for a duration of days: ((max harvest * sell price) - seed price) // duration\n
              """)
        
    @staticmethod
    def help():
        print("""
              This tool helps you to calculate the minimum profit from your crops based on your seed price and\n 
              Maturity days of your crops. Profit margin, duration and number of crops can also be included in\n
              the calculations but are not required.
              """)
