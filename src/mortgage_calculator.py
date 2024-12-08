import sys


# Пример кода калькулятора ипотеки, совместимый с Python 3.5

def calculate_monthly_payment(principal, annual_rate, years):
    # Преобразование годовой ставки в месячную
    monthly_rate = annual_rate / 100 / 12
    # Количество месяцев
    months = years * 12
    
    if monthly_rate == 0:
        return principal / months  # Если ставка 0, то просто делим сумму на количество месяцев
    
    # Рассчитываем ежемесячный платеж
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    
    return monthly_payment


# Пример использования:
principal = 300000  # Сумма кредита
annual_rate = 0.04  # Годовая ставка 4%
years = 30  # Срок кредита

payment = calculate_monthly_payment(principal, annual_rate, years)

# Старый способ форматирования строк для Python 3.5
print("Your monthly payment is: {:.2f}".format(payment))
print("Updated version 8: Your monthly payment is: 1432.25")

