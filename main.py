# Input validation for Loan Amount
while True:
    try:
        loan_amount = float(input("Enter loan amount: "))
        if loan_amount > 0:
            break
        print("Invalid! Loan amount must be positive.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Input validation for Annual Interest Rate
while True:
    try:
        annual_interest_rate = float(input("Enter annual interest rate (%): "))
        if annual_interest_rate >= 0:
            break
        print("Invalid! Interest rate can't be negative.")
    except ValueError:
        print("Invalid input! Please enter a number")

# Input validation for Loan Term Years
while True:
    try:
        loan_terms_years = float(input("Enter loan terms in (years): "))
        if loan_terms_years >= 1 and loan_terms_years <= 50:
            break
        print("Invalid! Loan term must be atleast 1 year or utmost 50 years")
    except ValueError:
        print("Invalid input! Please enter a number")

# Convert monthly rate
monthly_rate = annual_interest_rate / 12 / 100
# Calculate total number of payments
number_of_payments = loan_terms_years * 12

def calculate_monthly_payment(P, r, n):             # P = Loan Amount, r = Monthly Rate, n = Total Numbers of Payments
    # Calculate monthly payment
    if monthly_rate == 0:
        return loan_amount / number_of_payments
    else:
        return (loan_amount * monthly_rate * (1 + monthly_rate)**number_of_payments) / ((1 + monthly_rate)**number_of_payments - 1)

# Compute and display the monthly payment
monthly_payment = calculate_monthly_payment(P= loan_amount, r= monthly_rate, n= number_of_payments)
print(f"Your monthly payment is ${round(monthly_payment, 2)}")