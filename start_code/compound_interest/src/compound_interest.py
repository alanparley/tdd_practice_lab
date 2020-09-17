class CompoundInterest:

    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate / 100
        self.years = years
        self.times_compounded = 12

    def calculate(self):
        amount = self.principal * \
            (1 + (self.rate / self.times_compounded)
             )**(self.years*self.times_compounded)
        return round(amount, 2)

# Write a program to compute the value of an investment compounded over time. The program should ask for the starting amount, the number of years to invest and the interest rate. Assume it is compounded 12 times a year.

# The formula you’ll use for this is:

# A = P(1 + r/n)nt

# Where:

# P is the principal amount
# r is the annual rate of interest
# t is the number of years the amount is invested
# n is the number of times the interest is compounded per year
# A is the amount at the end of the investment
