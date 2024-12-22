print("The Zillow 'Buyability' Calculator")
print("Payment calculator")
principal = int(input("Home Price"))
down_payment = float(input("Down Payment"))
number_of_years = int(input("Mortgage Type"))
interest_rate = float(input("Interest Rate"))
percentage = float(input("Percentage"))
print(principal)
print(down_payment)
print(number_of_years)
print(interest_rate)
print(percentage)
loan_amount = principal - down_payment
monthly_interest_rate = (interest_rate / 100) / 12
total_payments = number_of_years * 12
numerator_interest = monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments
denominator_interest = (1 + monthly_interest_rate) ** total_payments - 1
monthly_payment = round(loan_amount * numerator_interest / denominator_interest, 2)
print(f"Your estimated monthly payment is {monthly_payment}")