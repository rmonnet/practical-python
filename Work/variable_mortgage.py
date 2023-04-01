# Dave has decided to take out a 30 years mortgage of $500,000.
# The interest rate is 5%, the monthly payment is $2684.11
# Calculate the total amount that Dave will have to pay over the
# life of the mortgage

# User input is used to set custom payments

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0
number_months = 0
extra_payment_start_month = 1000000000
extra_payment_end_month = extra_payment_start_month
extra_payment = 0

extra_payment = int(input('Extra payment / month: '))
if extra_payment > 0:
    extra_payment_start_month = int(input('Extra payment start month: '))
    extra_payment_end_month = int(input('Extrapoayment end month: '))

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    number_months = number_months + 1
    if number_months >= extra_payment_start_month and number_months <= extra_payment_end_month:
        total_paid = total_paid + extra_payment
        principal = principal - extra_payment
    print(number_months, round(total_paid, 2), round(principal, 2))


print('Total paid', round(total_paid, ndigits=2))
print('Number of Months', number_months)
