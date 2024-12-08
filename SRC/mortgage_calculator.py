def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    total_months = years * 12
    if monthly_rate == 0:
        return principal / total_months
    return principal * (monthly_rate * (1 + monthly_rate) ** total_months) / ((1 + monthly_rate) ** total_months - 1)

if __name__ == "__main__":
    principal = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (in %): "))
    years = int(input("Enter loan term (in years): "))
    payment = calculate_monthly_payment(principal, annual_rate, years)
    print(f"Your monthly payment is: {payment:.2f}")
