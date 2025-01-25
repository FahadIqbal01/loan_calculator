# Input validation for Loan Amount
while True:
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
        if r == 0:
            M = P / n
        else:
            M = (P * r * (1 + r)**n) / ((1 + r)**n - 1)
        
        total_repayment = round(M * n, 2)               # Total repayment over the load term
        return M, total_repayment
    # Compute and display the monthly payment
    monthly_payment, total_repayment = calculate_monthly_payment(P= loan_amount, r= monthly_rate, n= number_of_payments)
    print(f"Your monthly payment is ${round(monthly_payment, 2)}")
    print(f"Total repayment over {int(loan_terms_years)} years: ${total_repayment}")
    
    while True:
        query_for_another_calculation = input("Do you want to calculate another loan? (yes/no): ").lower()

        if query_for_another_calculation in ["yes", "y", "no", "n"]:
            break
        print("Invalid input! Please enter 'yes' or 'no'")
        
    if query_for_another_calculation in ["no", "n"]:
        print("Goodbye! Have a good day.")
        break