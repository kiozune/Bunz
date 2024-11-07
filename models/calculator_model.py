class Calculator:
    def __init__(self, principal, annual_interest_rate, years):
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years

    def calculate_loan(self, principal, annual_interest_rate, years):
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12
        monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment
