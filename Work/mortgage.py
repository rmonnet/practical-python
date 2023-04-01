# Dave has decided to take out a 30 years mortgage of $500,000.
# The interest rate is 5%, the monthly payment is $2684.11
# Calculate the total amount that Dave will have to pay over the
# life of the mortgage

# Suppose Dave has an extra payment of $1000/month for the first 12 months
# of the mortgage.

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0
number_months = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if number_months < 12:
        total_paid = total_paid + 1000
        principal = principal - 1000
    number_months = number_months + 1

print('Total paid', round(total_paid, ndigits=2))
print('Number of Months', number_months)
