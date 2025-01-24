# Inputs: 
# 50000
# 5%
# 10

# Outputs:
# $530.33

# 1. Take Inputs
loan_amount = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate (%): "))
loan_terms_years = float(input("Enter loan terms in (years): "))

def calculate_monthly_payment():
    # Convert monthly rate
    monthly_rate = annual_interest_rate / 12 / 100
    # Calculate total number of payments
    number_of_payments = loan_terms_years * 12
    # Calculate monthly payment
    monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate)**number_of_payments) / ((1 + monthly_rate)**number_of_payments - 1)
    print(f"Your monthly payment is ${round(monthly_payment, 3)}")


calculate_monthly_payment()